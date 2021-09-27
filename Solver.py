from datatypes import Timetable

class Solver:
    """
    Base class of all solve classes

    The data relevent for all sovlers should be stored here
    """
    def __init__(self, timetable: Timetable):
        self.timetable = timetable