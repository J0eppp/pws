import datatypes as types
from typing import List
import utils
from tabulate import tabulate

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
            # ds, hs, ts, gs, _ = lesson
            # day, hour, teacher, group, scheduled = lesson
            day = lesson.day
            hour = lesson.hour
            teacher = lesson.teacher
            group = lesson.group

            if (day == d and hour == h) and (group == g or teacher == t):
                return False
        
        return True

    def create_feasible_timetable(self) -> types.Timetable:
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
                                lesson = types.Lesson(teacher, group, day, hour, None)
                                # lessons.append((day, hour, teacher, group, None))
                                lessons.append(lesson)
        timetable = types.Timetable(lessons)
        return timetable
    
    @staticmethod
    def print_result(result: List[List], amount_of_groups: int):
        # Sort everything by group
        data = [[]] * amount_of_groups
        for res in result:
            data[res[3] - 1] = str(res[2])
        
        
        for group in data:
            print(tabulate(group))