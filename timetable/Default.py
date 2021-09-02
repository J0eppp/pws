from uuid import uuid4
from json import dumps


class Default:
    """
    Most classes inherit this
    """

    def __init__(self):
        self.id: str = uuid4().__str__()

    def json(self) -> str:
        return dumps(self.__dict__, indent=4)
