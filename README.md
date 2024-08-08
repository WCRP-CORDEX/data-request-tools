# data-request-tools

[![github CI](https://github.com/WCRP-CORDEX/data-request-tools/actions/workflows/ci.yaml/badge.svg)](https://github.com/WCRP-CORDEX/data-request-tools/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/github/WCRP-CORDEX/data-request-tools/graph/badge.svg?token=UDK6TMSH4R)](https://codecov.io/github/WCRP-CORDEX/data-request-tools)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/WCRP-CORDEX/data-request-tools/main.svg)](https://results.pre-commit.ci/latest/github/WCRP-CORDEX/data-request-tools/main)

Tools to manage a (CORDEX) data request in csv format. The main task of this package is to create [CORDEX-CMIP6 create tables](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/tree/main/Tables))
from a [data request table in csv format](https://github.com/WCRP-CORDEX/data-request-table/blob/main/CORDEX-CMIP6/data-request.csv). In general, this package should also be useful to
create other tables from other data requests.

## API Example

This tools helps to convert a CMIP data request in csv format into a number of CMOR tables in json format.

```python
import data_request as dr
import pandas as pd

table = "https://raw.githubusercontent.com/WCRP-CORDEX/data-request-table/main/CORDEX-CMIP6/data-request.csv"

df = pd.read_csv(table).fillna("")
cmor_tables = dr.create_cmor_tables(df)
cmor_tables.keys()
```
gives
```
dict_keys(['1hr', '6hr', 'day', 'fx', 'mon'])
```
The tables can be written to CMOR json tables using:
```python
for t in cmor_tables.values():
    dr.table_to_json(t, table_prefix="CORDEX-CMIP6")
```
which creates a tables based on the `table_id` in the header:
```
writing: ./CORDEX-CMIP6_1hr.json
writing: ./CORDEX-CMIP6_6hr.json
writing: ./CORDEX-CMIP6_day.json
writing: ./CORDEX-CMIP6_fx.json
writing: ./CORDEX-CMIP6_mon.json
```
The coordinates table can also be created by searching through the `dimensions` column:
```python
coords = dr.create_coordinate_table(df)
```
results in
```
found: ['height100m', 'height10m', 'height150m', 'height200m', 'height250m', 'height2m', 'height300m', 'height50m', 'latitude', 'longitude', 'p10', 'p100', 'p1000', 'p150', 'p20', 'p200', 'p250', 'p30', 'p300', 'p400', 'p50', 'p500', 'p600', 'p70', 'p700', 'p750', 'p850', 'p925', 'sdepth', 'time', 'time1']
```
and can be written using:
```python
dr.table_to_json(coords, "CORDEX-CMIP6", table_id="coordinate")
```

## Command line

You can also use the command `create-cmor-tables` in a terminal to create cmor tables from anything that `pandas.read_csv` can understand, e.g.

```
create-cmor-tables https://raw.githubusercontent.com/WCRP-CORDEX/data-request-table/main/CORDEX-CMIP6/data-request.csv --coords
```

will do the same as above.
