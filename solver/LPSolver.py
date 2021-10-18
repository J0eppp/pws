from itertools import combinations
from .Solver import Solver
from dataclasses import dataclass
from .datatypes import Timetable, Lesson
from mip import Model, minimize, BINARY, xsum
from . import utils
import time

SEPERATION_STRING = "-==================================-"


class LPSolver(Solver):
    def __init__(self, timetable: Timetable):
        self.timetable = timetable
        self.model = Model("timetable")
        self.model.verbose = 0

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        # Create all possibilities
        utils.uprint(SEPERATION_STRING)
        utils.uprint("Creating all possibilities")
        start_time = time.process_time()

        S = []
        for group in self.timetable.groups:
            for subject in group.subjects:
                for si in self.timetable.subject_information:
                    if si.subject != subject:
                        continue
                    teacher = [
                        teacher for teacher in self.timetable.teachers if teacher.subject == subject][0]
                    for _ in range(si.amount):
                        for day in range(self.timetable.amount_of_days_a_week):
                            for hour in range(self.timetable.amount_of_hours_a_day):
                                lesson = Lesson(
                                    len(S) - 1, teacher, group, day, hour, self.model.add_var(BINARY))
                                teacher.lessons.append(lesson)
                                group.lessons.append(lesson)
                                S.append(lesson)

        end_time = time.process_time()
        utils.uprint(f"Created {len(S)} possibilities")
        utils.uprint(
            f"Creating all possibilities took {end_time - start_time} seconds")

        # Creating constraints
        nr_constraints = 0
        utils.uprint(SEPERATION_STRING)
        utils.uprint("Creating constraints")
        start_time = time.process_time()

        # The first constraint makes sure that a lesson should be scheduled a specific amount of times
        for group in self.timetable.groups:
            for teacher in self.timetable.teachers:
                amount = 0
                for subject_info in self.timetable.subject_information:
                    if subject_info.subject == teacher.subject and subject_info.year == group.year:
                        amount = subject_info.amount
                        break
                print(sum([1 for lesson in S if lesson.group ==
                           group and lesson.teacher == teacher]))
                self.model += xsum([1 for lesson in S if lesson.group ==
                                   group and lesson.teacher == teacher]) == amount
                nr_constraints += 1

        # Making sure lessons do not conflict in the second constraint
        for (lesson1, lesson2) in combinations(S, r=2):
            if ((lesson1.group == lesson2.group or lesson1.teacher == lesson2.teacher) and (lesson1.day == lesson2.day and lesson1.hour == lesson2.hour)):
                # Conflict, we can only use one of the lessons
                self.model += lesson1.scheduled + lesson2.scheduled <= 1
                nr_constraints += 1

        end_time = time.process_time()
        utils.uprint("Done creating constraints")
        utils.uprint(f"Created {nr_constraints} constraints")
        utils.uprint(
            f"Creating constraints took {end_time - start_time} seconds")
        utils.uprint(SEPERATION_STRING)

        # Objective function
        # self.model.objective = self.timetable.count_gap_hours()
        self.model.objective = minimize(
            xsum([group.count_gap_hours(self.timetable.amount_of_days_a_week) for group in self.timetable.groups]))

        utils.uprint(SEPERATION_STRING)
        utils.uprint("Optimizing")
        start_time = time.process_time()
        self.model.optimize()
        selected = [
            lesson for lesson in self.timetable.lessons if lesson.scheduled.x >= 0.99]

        utils.uprint(f"Amount of hours selected: {len(selected)}")
        utils.uprint(SEPERATION_STRING)

        return self.timetable
