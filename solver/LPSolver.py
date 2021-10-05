from Solver import Solver
from dataclasses import dataclass
from datatypes import Timetable, Lesson
from mip import Model, minimize
import utils


class LPSolver(Solver):
    """The linear programming solver"""

    def __init__(self, timetable: Timetable):
        self.timetable = timetable
        self.model = Model()

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        utils.uprint(f"Feasible timetable: {self.timetable.create_feasible_timetable()}")
        utils.uprint(
            f"Amount of gap hours: {self.timetable.count_gap_hours()}")
        return self.timetable
