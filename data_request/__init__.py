from importlib.metadata import version as _get_version

from .cleaning import retrieve_data_request
from .const import table_prefix
from .coordinates import get_coordinate_table
from .table_creation import create_cmor_tables

try:
    __version__ = __version__ = _get_version("data-request-tools")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "999"

__all__ = [
    "create_cmor_tables",
    "get_coordinate_table",
    "table_prefix",
    "retrieve_data_request",
]
