import mip
import utils
from time import sleep
import timetable_types

from Solver import Solver

class LPSolver(Solver):
    """
    The lineair programming solution class of our problem
    """
    def __init__(self, timetable: timetable_types.Timetable):
        super().__init__()
        self.model = None
        self.timetable = timetable
    
    def solve(self):
        return self.__solve(self.timetable)
    
    def __solve(self, timetable: timetable_types.Timetable):
        self.model = mip.Model(sense=mip.MAXIMIZE, solver_name=mip.CBC)
        
        return []