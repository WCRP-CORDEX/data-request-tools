import pandas as pd

from .. import create_cmor_tables

data_request_table = "https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip6-data-request/main/tables/cordex-cmip6-data-request-extended.csv"


def test_create_cordex_cmor_table(table):
    print(f"retrieving data request from {table}")
    df = pd.read_csv(table).fillna("")
    create_cmor_tables(df)
    return
