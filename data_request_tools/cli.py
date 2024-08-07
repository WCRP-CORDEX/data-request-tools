import argparse

import pandas as pd

from . import create_cmor_tables, create_coordinate_table, table_to_json


def main(table, output, prefix, coords=False):
    df = pd.read_csv(table).fillna("")
    cmor_tables = create_cmor_tables(df)
    print(cmor_tables.keys())

    for t in cmor_tables.values():
        table_to_json(t, table_prefix=prefix, dir=output)

    if coords is True:
        t = create_coordinate_table(df)
        table_to_json(t, prefix, table_id="coordinate", dir=output)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("table", help="data request csv table")
    parser.add_argument("--prefix", help="table prefix", default="CORDEX-CMIP6")
    parser.add_argument("--output", help="output directory", default="Tables")
    parser.add_argument("--coords", action="store_true", help="create coordinate table")
    args = parser.parse_args()
    main(args.table, args.output, args.prefix, args.coords)
