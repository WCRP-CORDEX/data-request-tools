import json
import os
import re

import yaml

from .const import table_prefix


def parse_cell_methods(cm_string):
    # https://stackoverflow.com/questions/52340963/how-to-insert-a-newline-character-before-a-words-that-contains-a-colon
    ys = re.sub(r"(\w+):", r"\n\1:", cm_string).strip()
    d = yaml.safe_load(ys)

    if "area" in d and d.get("area") is None:
        d["area"] = d["time"]

    return d


def table_to_json(table, dir=None, prefix=None):
    if dir is None:
        dir = "./"
    if prefix is None:
        prefix = table_prefix
    if not os.path.isdir(dir):
        os.makedirs(dir)
    table_id = table["Header"]["table_id"].split()[1]
    filename = os.path.join(dir, f"{prefix}_{table_id}.json")
    print(f"writing: {filename}")
    with open(filename, "w") as fp:
        json.dump(table, fp, indent=4)
