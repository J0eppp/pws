from .datatypes import Timetable
from dataclasses import dataclass
from typing import Protocol


# @dataclass
class Solver(Protocol):
    """Baseclass of all the solvers"""
    timetable: Timetable

    def __init__(self, timetable: Timetable) -> None:
        ...

    def solve(self) -> Timetable:
        ...

    def __solve(self) -> Timetable:
        ...
