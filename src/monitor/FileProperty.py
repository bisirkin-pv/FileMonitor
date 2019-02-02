from typing import NamedTuple, Any


class FileProperty(NamedTuple):
    """
    Совойства файла
    """
    path: str
    name: str
    change_date: Any
