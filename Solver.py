import datatypes as types
from typing import List

class Solver:
    """
    Base class of all solve classes

    The data relevent for all sovlers should be stored here
    """
    def __init__(self, timetable: types.Timetable, amount_of_hours_a_day: int, amount_of_days_a_week: int, groups: List[int], teachers: List[int], amount: List[int]):
        self.timetable = timetable
        self.amount_of_hours_a_day = amount_of_hours_a_day
        self.amount_of_days_a_week = amount_of_days_a_week
        self.groups = groups
        self.teachers = teachers
        self.amount = amount # How often a class should get a lesson per week

    @staticmethod
    def can_schedule(d, h, t, g, lessons) -> bool:
        """Check if this lesson is allowed to be scheduled"""
        for lesson in lessons:
            # ds, hs, ts, gs = lesson.day, lesson.hour, lesson.teacher, lesson.group
            ds, hs, ts, gs, _ = lesson

            if (ds == d and hs == h) and (gs == g or ts == t):
                return False
        
        return True

    def create_feasible_timetable(self) -> List[tuple]:
        """Create a feasible timetable as a starting point for the algorithm"""
        lessons = []
        for group in self.groups:
            for i in range(len(self.teachers)):
                teacher = self.teachers[i]
                amount = self.amount[i]
                for _ in range(amount):
                    scheduled = False
                    for day in range(self.amount_of_days_a_week):
                        if scheduled == True: continue
                        for hour in range(self.amount_of_hours_a_day):
                            if scheduled == True: continue
                            if self.can_schedule(day, hour, teacher, group, lessons) == True:
                                scheduled = True
                                lessons.append((day, hour, teacher, group, None))
        return lessons