# data-request-tools

[![github CI](https://github.com/WCRP-CORDEX/data-request-tools/actions/workflows/ci.yaml/badge.svg)](https://github.com/WCRP-CORDEX/data-request-tools/actions/workflows/ci.yaml)

Tools to manage a (CORDEX) data request in csv format.

## Example

This tools helps to convert a CMIP data request in csv format into a number of CMOR tables in json format.

```python
import data_request as dr
import pandas as pd

table = "https://raw.githubusercontent.com/WCRP-CORDEX/data-request-table/sdepth/CORDEX-CMIP6/data-request.csv"

df = pd.read_csv(table).fillna("")
cmor_tables = dr.create_cmor_tables(df)
cmor_tables.keys()
```
```
dict_keys(['1hr', '6hr', 'day', 'fx', 'mon'])
```
