from typing import NamedTuple, Any


class FileProperty(NamedTuple):
    path: str
    name: str
    change_date: Any
