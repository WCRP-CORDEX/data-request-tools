import json
import os

from .const import conventions, mip_era

cordex_table_prefix = "CORDEX-CMIP6"
cordex_data_request_table = "https://raw.githubusercontent.com/WCRP-CORDEX/data-request-table/main/CORDEX-CMIP6/data-request.csv"

# columns in cmor tables according to CMIP6
columns = [
    "frequency",
    "modeling_realm",
    "standard_name",
    "units",
    "cell_methods",
    "cell_measures",
    "long_name",
    "comment",
    "dimensions",
    "out_name",
    "type",
    "positive",
    "valid_min",
    "valid_max",
    "ok_min_mean_abs",
    "ok_max_mean_abs",
]


def create_table_header(name, frequency):
    from datetime import date

    intervals = {
        "fx": "",
        "1hr": 0.041667,
        "3hr": 0.125,
        "6hr": 0.25,
        "day": 1.0,
        "mon": 30.0,
    }
    print(frequency)
    today = date.today()
    header = {
        #  "data_specs_version": __version__,
        # "cmor_version": "3.5",
        "table_id": f"Table {name}",
        # "realm": "atmos",
        "table_date": today.strftime("%d %B %Y"),
        "missing_value": "1e20",
        "int_missing_value": "-999",
        "product": "model-output",
        "approx_interval": f"{intervals[frequency]}",
        # "generic_levels": "",
        "mip_era": mip_era,
        "Conventions": conventions,
    }
    return header.copy()


def create_cmor_table(name, df):
    df = df.copy()
    df["index"] = df.out_name
    return dict(
        Header=create_table_header(name, name),
        variable_entry=df.set_index("index")[columns].to_dict(orient="index"),
    )


def create_cmor_tables(df, groupby=None):
    """Create cmor tables depending on grouped attribute"""

    df = df.copy()

    if groupby is None:
        df["group"] = df.frequency.str.slice(start=0, stop=3)
        groupby = "group"

    def name(g):
        if isinstance(g, tuple):
            return "_".join(g)
        return g

    gb = df.groupby(groupby)
    return {name(g): create_cmor_table(name(g), gb.get_group(g)) for g in gb.groups}


def table_to_json(table, table_prefix, table_id=None, dir=None):
    if dir is None:
        dir = "./"
    if not os.path.isdir(dir):
        os.makedirs(dir)
    if table_id is None:
        table_id = table["Header"]["table_id"].split()[1]
    filename = os.path.join(dir, f"{table_prefix}_{table_id}.json")
    print(f"writing: {filename}")
    with open(filename, "w") as fp:
        json.dump(table, fp, indent=4)
