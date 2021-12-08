from typing import Protocol


class Program(Protocol):
    """Baseclass of this program"""

    def __init__(self):
        ...

    def log(self, msg: str):
        ...
