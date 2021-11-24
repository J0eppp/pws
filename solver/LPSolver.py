from itertools import combinations
from .Solver import Solver
from dataclasses import dataclass
from .Prettyprint import pretty_print
from .datatypes import Timetable, Lesson
from mip import Model, minimize, maximize, BINARY, xsum, INTEGER
from . import utils
import time

SEPERATION_STRING = "-==================================-"


class LPSolver(Solver):
    def __init__(self, timetable: Timetable):
        self.timetable = timetable
        self.model = Model("timetable")
        # self.model.verbose = 1

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        # Create all possibilities
        utils.uprint(SEPERATION_STRING)
        utils.uprint("Creating all possibilities")
        start_time = time.time()

        groups = self.timetable.groups
        teachers = self.timetable.teachers
        subject_infos = self.timetable.subject_information

        # We forget the timetable instance for now.
        S = []
        for group in groups:
            for subject in group.subjects:
                for si in subject_infos:
                    if si.subject != subject:
                        continue
                    teacher = [
                        teacher for teacher in self.timetable.teachers if teacher.subject == subject][0]
                    for _ in range(si.amount):
                        for day in range(self.timetable.amount_of_days_a_week):
                            for hour in range(self.timetable.amount_of_hours_a_day):
                                lesson = Lesson(
                                    len(S) - 1, teacher, group, day, hour, si, self.model.add_var(var_type=BINARY))
                                teacher.lessons.append(lesson)
                                group.lessons.append(lesson)
                                S.append(lesson)

        end_time = time.time()
        utils.uprint(f"Created {len(S)} possibilities")
        utils.uprint(
            f"Creating all possibilities took {end_time - start_time} seconds")

        # Creating constraints
        nr_constraints = 0
        utils.uprint(SEPERATION_STRING)
        utils.uprint("Creating constraints")
        start_time = time.time()

        # The first constraint makes sure that a lesson should be scheduled a specific amount of times
        for group in groups:
            for teacher in teachers:
                amount = 0
                for subject_info in subject_infos:
                    if subject_info.subject == teacher.subject and subject_info.year == group.year:
                        amount = subject_info.amount
                        break
                self.model += xsum([lesson.scheduled for lesson in S if lesson.group ==
                                   group and lesson.teacher == teacher]) == amount
                nr_constraints += 1

        # Making sure lessons do not conflict in the second constraint
        for (lesson1, lesson2) in combinations(S, r=2):
            if ((lesson1.group == lesson2.group or lesson1.teacher == lesson2.teacher) and (lesson1.day == lesson2.day and lesson1.hour == lesson2.hour)):
                # Conflict, we can only use one of the lessons
                self.model += lesson1.scheduled + lesson2.scheduled <= 1
                nr_constraints += 1

        end_time = time.time()
        utils.uprint("Done creating constraints")
        utils.uprint(f"Created {nr_constraints} constraints")
        utils.uprint(
            f"Creating constraints took {end_time - start_time} seconds")
        utils.uprint(SEPERATION_STRING)

        # Objective function
        self.model.objective = minimize(
            xsum([group.count_gap_hours(self.timetable.amount_of_days_a_week, self.timetable.amount_of_hours_a_day)
                 for group in groups])
        )
        # Minimize the count of hours
        # Effectively this will try to put all the hours earlier on the day
        # self.model.objective = minimize(
        #     xsum(
        #         [(lesson.hour * lesson.hour) * lesson.scheduled for lesson in group.lessons for group in groups])
        # )

        utils.uprint(SEPERATION_STRING)
        utils.uprint("Optimizing")
        start_time = time.time()
        print(self.model.optimize())
        end_time = time.time()
        utils.uprint("Done optimizing")
        utils.uprint(f"Optimizing took {end_time - start_time} seconds")
        utils.uprint(SEPERATION_STRING)
        selected = [
            lesson for lesson in S if lesson.scheduled.x >= 0.99]

        # Add found schedule to timetable.
        self.timetable.lessons = selected
        [group.select_lessons() for group in groups]
        [teacher.select_lessons() for teacher in teachers]

        utils.uprint(SEPERATION_STRING)
        utils.uprint(f"Amount of hours selected: {len(selected)}")
        utils.uprint(SEPERATION_STRING)
        pretty_print(self.timetable)
        return self.timetable
