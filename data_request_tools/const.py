height_key_template = "height{value}m"
pressure_key_template = "p{value}"

table_prefix = "CORDEX"

conventions = "CF-1.11"

mip_era = "CMIP6"

height = {
    "standard_name": "height",
    "units": "m",
    "axis": "Z",
    "long_name": "height",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "height",
    "positive": "up",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}


pressure = {
    "standard_name": "air_pressure",
    "units": "Pa",
    "axis": "Z",
    "long_name": "pressure",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "plev",
    "positive": "down",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "",
    "tolerance": "",
    "type": "double",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}


longitude = {
    "standard_name": "longitude",
    "units": "degrees_east",
    "axis": "X",
    "long_name": "Longitude",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "lon",
    "positive": "",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "360.0",
    "valid_min": "0.0",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}

latitude = {
    "standard_name": "latitude",
    "units": "degrees_north",
    "axis": "Y",
    "long_name": "Latitude",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "lat",
    "positive": "",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "90.0",
    "valid_min": "-90.0",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}


time = {
    "standard_name": "time",
    "units": "days since ?",
    "axis": "T",
    "long_name": "time",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "yes",
    "out_name": "time",
    "positive": "",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}

time1 = {
    "standard_name": "time",
    "units": "days since ?",
    "axis": "T",
    "long_name": "time",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "time",
    "positive": "",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}

time2 = {
    "standard_name": "time",
    "units": "days since ?",
    "axis": "T",
    "long_name": "time",
    "climatology": "yes",
    "formula": "",
    "must_have_bounds": "yes",
    "out_name": "time",
    "positive": "",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}

sdepth = {
    "standard_name": "depth",
    "units": "m",
    "axis": "Z",
    "long_name": "depth",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "yes",
    "out_name": "depth",
    "positive": "down",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "double",
    "valid_max": "200.0",
    "valid_min": "0.0",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}

depth_coord = {
    "standard_name": "depth",
    "units": "m",
    "axis": "Z",
    "long_name": "ocean depth coordinate",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "yes",
    "out_name": "lev",
    "positive": "down",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "increasing",
    "tolerance": "",
    "type": "",
    "valid_max": "12000.0",
    "valid_min": "0.0",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "olevel",
}

type = {
    "standard_name": "area_type",
    "units": "",
    "axis": "",
    "long_name": "Sea Ice area type",
    "climatology": "",
    "formula": "",
    "must_have_bounds": "no",
    "out_name": "type",
    "positive": "",
    "requested": "",
    "requested_bounds": "",
    "stored_direction": "",
    "tolerance": "",
    "type": "character",
    "valid_max": "",
    "valid_min": "",
    "value": "",
    "z_bounds_factors": "",
    "z_factors": "",
    "bounds_values": "",
    "generic_level_name": "",
}

typesi = type.copy()
typesi["long_name"] = "Sea Ice area type"
typesi["value"] = "sea_ice"

typelake = type.copy()
typelake["long_name"] = "Lake and Inland Sea area type"
typelake["value"] = "lake_and_inland_sea"

typeurban = type.copy()
typeurban["long_name"] = "Urban area type"
typeurban["value"] = "urban"

dim_table = {
    "longitude": longitude,
    "latitude": latitude,
    "heightm": height,
    "p": pressure,
    "time": time,
    "time1": time1,
    "time2": time2,
    "sdepth": sdepth,
    "olevel": depth_coord,
    "typesi": typesi,
    "typelake": typelake,
    "typeurban": typeurban,
}
