import mip
from mip import Model, xsum, minimize, BINARY, INTEGER, MINIMIZE, CBC
import utils
import time
import datatypes as types
from math import floor
from typing import List

from Solver import Solver

class LPSolver(Solver):
    """
    The lineair programming solution class of our problem
    """
    def __init__(self, timetable: types.Timetable, amount_of_hours_a_day: int, amount_of_days_a_week: int, groups: List[int], teachers: List[int], amount: List[int]):
        super().__init__(timetable, amount_of_hours_a_day, amount_of_days_a_week, groups, teachers, amount)
        self.model = None
        # self.amount_of_hours_a_day = amount_of_hours_a_day
        # self.amount_of_days_a_week = amount_of_days_a_week
        # self.groups = groups
        # self.teachers = teachers
        # self.amount = amount # How often a class should get a lesson per week
        self.amount_of_lessons_to_schedule = len(self.groups) * sum(self.amount)

    def solve(self):
        return self.__solve(self.timetable)
    
    def __calc_hour(self, hour) -> int:
        return round(((hour / self.amount_of_hours_a_day) - floor(hour / self.amount_of_hours_a_day)) * self.amount_of_hours_a_day)
    
    def __calc_day(self, hour) -> int:
        return floor(hour / self.amount_of_hours_a_day)
    
    @staticmethod
    def countGapHours(lessons) -> int:
        """Count all the gap hours in the timetable"""
        timetable = [[[]]]
        
        gap_hours = 0

        for lesson in lessons:
            d, h, g, _, _ = lesson

            timetable[g][d].append(h)

            for g in timetable:
                for d in timetable[g]:
                    arr = timetable[g][d]
                    arr = arr.sort()
                    first = arr[0]
                    last = arr[-1]
                    amount = last - (first - 1) - len(arr)
                    gap_hours += amount
        
        return gap_hours

    def __solve(self, timetable: types.Timetable):
        self.model = Model(sense=MINIMIZE)
        self.model.verbose = 0
        
        # Variables
        H = self.amount_of_days_a_week * self.amount_of_hours_a_day

        utils.uprint("-==================================-")
        utils.uprint("Creating variables")
        start_time = time.process_time()

        S = []
        for group in self.groups:
            # for teacher in self.teachers:
            for i in range(len(self.teachers)):
                teacher = self.teachers[i]
                for j in range(self.amount[i]): # how often a subject should be schedules for each class
                    scheduled = False
                    for day in range(self.amount_of_days_a_week):
                        if scheduled == True:
                            continue
                        for hour in range(self.amount_of_hours_a_day):
                            if scheduled == True:
                                continue
                            if self.can_schedule(day, hour, teacher, group, S) == True:
                                S.append((day, hour, teacher, group, self.model.add_var(var_type=BINARY)))
                                scheduled = True
                    if scheduled == False:
                        utils.uprint(f"ERROR: WAS NOT ABLE TO SCHEDULE A CLASS")

        end_time = time.process_time()
        utils.uprint("Done creating variables")
        utils.uprint(f"Created {len(S)} variables")
        utils.uprint(f"Creating variables took: {end_time - start_time} seconds")
        utils.uprint("-==================================-")

        # Constrains
        nr_constraints = 0
        utils.uprint("-==================================-")
        utils.uprint("Creating constraints")
        start_time = time.process_time()
        # TODO fix this first constraint
        # # The first contraint is that the length of S has to be equal to the amount of lessons that has to be scheduled
        # self.model += len(S) - self.amount_of_lessons_to_schedule == 0
        # nr_constraints += 1

        utils.uprint(f"Contstraint 1: {len(S) - self.amount_of_lessons_to_schedule == 0}")

        # The second constraint makes sure that a lesson should be schedules a specific amount of times
        for group in self.groups:
            for i in range(len(self.teachers)):
                teacher = self.teachers[i]
                amount = self.amount[i]
                self.model += xsum([1 for (_, _, g, t, var) in S if g == group and t == teacher]) == amount
                nr_constraints += 1

        end_time = time.process_time()
        utils.uprint("Done creating constraints")
        utils.uprint(f"Created {nr_constraints} constraints")
        utils.uprint(f"Creating constraints took {end_time - start_time} seconds")
        utils.uprint("-==================================-")

        # Create feasible solution to start with
        utils.uprint("-==================================-")
        utils.uprint("Creating feasible solution as a starting point")
        start_time = time.process_time()
        feasible_selected = self.create_feasible_timetable()
        end_time = time.process_time()
        utils.uprint("Done creating feasible solution")
        utils.uprint(f"Feasible amount: {len(feasible_selected)}")
        utils.uprint(f"Creating the feasible solution took {end_time - start_time} seconds")
        utils.uprint("-==================================-")

        self.model.start = [(var, 1.0) for (d, h, t, g, var) in S if (d, h, t, g) in feasible_selected]


        # Objective function
        self.model.objective = self.timetable.countGapHours()

        self.model.optimize()

        selected = [(d, h, g, t, var) for (d, h, g, t, var) in S if var.x >= 0.99]

        utils.uprint(f"Amount of hours selected: {len(selected)}")

        return self.model