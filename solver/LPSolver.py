from Solver import Solver
from dataclasses import dataclass
from datatypes import Timetable, Lesson
from mip import Model, minimize


class LPSolver(Solver):
    """The linear programming solver"""

    def __init__(self, timetable: Timetable):
        self.timetable = timetable
        self.model = Model()

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        lesson = Lesson(
            1, self.timetable.teachers[0], self.timetable.groups[0], 0, 0)
        self.timetable.schedule_lesson(lesson)
        lesson = Lesson(
            2, self.timetable.teachers[0], self.timetable.groups[0], 2, 0)
        self.timetable.schedule_lesson(lesson)
        print("Amount of gap hours: ", self.timetable.count_gap_hours())
        return self.timetable
