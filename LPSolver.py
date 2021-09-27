import mip
import utils
from time import sleep
import datatypes as types

from Solver import Solver

class LPSolver(Solver):
    """
    The lineair programming solution class of our problem
    """
    def __init__(self, timetable: types.Timetable):
        super().__init__(timetable)
        self.model = None
        # self.timetable = timetable
    
    def solve(self):
        return self.__solve(self.timetable)
    
    def __solve(self, timetable: types.Timetable):
        self.model = mip.Model(sense=mip.MAXIMIZE, solver_name=mip.CBC)
        
        return timetable