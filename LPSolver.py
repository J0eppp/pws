import mip
from mip import Model, xsum, minimize, INTEGER
import utils
from time import sleep
import datatypes as types
from math import floor

from Solver import Solver

class LPSolver(Solver):
    """
    The lineair programming solution class of our problem
    """
    def __init__(self, timetable: types.Timetable, amount_of_hours_a_day: int, amount_of_days_a_week: int):
        super().__init__(timetable)
        self.model = None
        self.amount_of_hours_a_day = amount_of_hours_a_day
        self.amount_of_days_a_week = amount_of_days_a_week

    def solve(self):
        return self.__solve(self.timetable)
    
    def __calc_hour(self, hour) -> int:
        return round(((hour / self.amount_of_hours_a_day) - floor(hour / self.amount_of_hours_a_day)) * self.amount_of_hours_a_day)
    
    def __calc_day(self, hour) -> int:
        return floor(hour / self.amount_of_hours_a_day)

    def __solve(self, timetable: types.Timetable):
        self.model = Model()
        
        # Variables
        H = self.amount_of_days_a_week * self.amount_of_hours_a_day

        utils.uprint("Creating variables")
        start_time = time.process_time()

        S = []
        

        end_time = time.process_time()
        utils.uprint("Done creating variables")
        utils.urpint(f"Creating variables took: {end_time - start_time} seconds")

        # Constrains


        # Objective function
        self.model.objective = minimize(self.timetable.countGapHours())

        self.model.optimize()

        return self.model