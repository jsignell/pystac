# mypy: ignore-errors
from pystac.utils import _import_optional_dependency

pystac_client = _import_optional_dependency("pystac_client")

from pystac_client import *  # noqa: E402,F403


def __getattr__(value: str):
    return getattr(pystac_client, value)
