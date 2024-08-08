from .const import table_prefix
from .coordinates import create_coordinate_table
from .table_creation import create_cmor_tables, table_to_json


def _get_version():
    __version__ = "unknown"
    try:
        from ._version import __version__
    except ImportError:
        pass
    return __version__


__version__ = _get_version()

__all__ = [
    "create_cmor_tables",
    "create_coordinate_table",
    "table_prefix",
    #    "retrieve_data_request",
    "table_to_json",
]
