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
gives
```
dict_keys(['1hr', '6hr', 'day', 'fx', 'mon'])
```

Create the Coordinates table by searching through the `dimensions` column:
```python
coords = dr.get_coordinate_table(df)
```
results in
```
found: ['height100m', 'height10m', 'height150m', 'height200m', 'height250m', 'height2m', 'height300m', 'height50m', 'latitude', 'longitude', 'p10', 'p100', 'p1000', 'p150', 'p20', 'p200', 'p250', 'p30', 'p300', 'p400', 'p50', 'p500', 'p600', 'p70', 'p700', 'p750', 'p850', 'p925', 'sdepth', 'time', 'time1']
```
