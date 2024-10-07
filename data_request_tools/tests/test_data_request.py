import pandas as pd

from .. import create_cmor_tables, create_coordinate_table, table_to_json

cordex_data_request_table = "https://raw.githubusercontent.com/WCRP-CORDEX/data-request-table/refs/heads/main/cmor-table/datasets.csv"


def test_create_cordex_cmor_table():
    table = cordex_data_request_table
    print(f"retrieving data request from {table}")
    df = pd.read_csv(table).fillna("")
    cmor_tables = create_cmor_tables(df)
    for t in cmor_tables.values():
        table_to_json(t, table_prefix="CORDEX-CMIP6")
    return


def test_create_coordinate_table():
    table = cordex_data_request_table
    print(f"retrieving data request from {table}")
    df = pd.read_csv(table).fillna("")
    coords = create_coordinate_table(df)
    table_to_json(coords, "CORDEX-CMIP6", table_id="coordinate")
    return
