from .Solver import Solver
from dataclasses import dataclass
from .datatypes import Timetable, Lesson
from mip import Model, MINIMIZE, BINARY, xsum
# import utils
from . import utils
import time

SEPERATION_STRING = "-==================================-"


class LPSolver(Solver):
    """The linear programming solver"""

    def __init__(self, timetable: Timetable):
        self.timetable = timetable
        self.model = Model(sense=MINIMIZE)
        self.model.verbose = 0

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        # Creating variables
        # H: int = self.timetable.amount_of_days_a_week * \
        #     self.timetable.amount_of_hours_a_day

        # utils.uprint(SEPERATION_STRING)
        # utils.uprint("Creating variables")
        # start_time = time.process_time()

        # Scheduled lessons
        # S = []
        # for group in self.timetable.groups:
        #     for teacher in self.timetable.teachers:
        #         amount: int = [
        #             si.amount for si in self.timetable.subject_information if si.subject == teacher.subject][0]
        #         for i in range(amount):
        #             scheduled = False
        #             for day in range(self.timetable.amount_of_days_a_week):
        #                 if scheduled == True:
        #                     continue
        #                 for hour in range(self.timetable.amount_of_hours_a_day):
        #                     if scheduled == True:
        #                         continue
        #                     for lesson in S:
        #                         if (day == lesson.day and hour == lesson.hour) and (group == lesson.group or teacher == lesson.teacher):
        #                             lesson = Lesson(
        #                                 len(S) - 1, teacher, group, day, hour, self.model.add_var(var_type=BINARY))
        #                             S.append(lesson)
        #                             scheduled = True
        #             if scheduled == False:
        #                 utils.uprint(
        #                     f"ERROR: WAS NOT ABLE TO SCHEDULE A CLASS")

        # end_time = time.process_time()
        # utils.uprint("Done creating variables")
        # utils.uprint(f"Created {len(S)} variables")
        # utils.uprint(
        #     f"Creating variables took: {end_time - start_time} seconds")
        # utils.uprint(SEPERATION_STRING)

        utils.uprint(SEPERATION_STRING)
        utils.uprint("Creating feasible timetable")
        start_time = time.process_time()
        self.timetable.create_feasible_timetable(self.model.add_var, BINARY)
        end_time = time.process_time()
        utils.uprint("Done creating feasible timetable")
        utils.uprint(f"Scheduled {len(self.timetable.lessons)} lessons")
        utils.uprint(
            f"Creating feasible schedule took {end_time - start_time} seconds")
        utils.uprint(SEPERATION_STRING)

        # utils.uprint(SEPERATION_STRING)
        # utils.uprint("Calculating amount of gap hours")
        # start_time = time.process_time()
        # gap_hours = self.timetable.count_gap_hours()
        # end_time = time.process_time()
        # utils.uprint("Done calculating amount of gap hours")
        # utils.uprint(
        #     f"Amount of gap hours: {gap_hours}")
        # utils.uprint(
        #     f"Calculating amount of gap hours took {end_time - start_time} seconds")
        # utils.uprint(SEPERATION_STRING)

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
                self.model += xsum([1 for lesson in self.timetable.lessons if lesson.group ==
                                   group and lesson.teacher == teacher]) == amount
                nr_constraints += 1

        end_time = time.process_time()
        utils.uprint("Done creating constraints")
        utils.uprint(f"Created {nr_constraints} constraints")
        utils.uprint(
            f"Creating constraints took {end_time - start_time} seconds")
        utils.uprint(SEPERATION_STRING)

        # Optimizing
        self.model.start = [(lesson.scheduled, 1.0)
                            for lesson in self.timetable.lessons]

        # Objective functions
        self.model.objective = self.timetable.count_gap_hours()

        utils.uprint(SEPERATION_STRING)
        utils.uprint("Optimizing")
        start_time = time.process_time()
        self.model.optimize()
        selected = [
            lesson for lesson in self.timetable.lessons if lesson.scheduled.x >= 0.99]

        utils.uprint(f"Amount of hours selected: {len(selected)}")
        utils.uprint(SEPERATION_STRING)

        return self.timetable
