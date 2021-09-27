from enum import Enum, auto
from dataclasses import dataclass
from typing import List

# Enum with all subjects
# class Subject(Enum):
#     NEDERLANDS = auto()
#     WISKUNDE = auto()
#     ENGELS = auto()
#     NASK = auto()
#     GESCHIEDENIS = auto()
#     BIOLOGIE = auto()
#     AARDRIJKSKUNDE = auto()
#     FRANS = auto()
#     DUITS = auto()

@dataclass
class Teacher:
    name: str
    lessons: List[int] # the index of the lesson

@dataclass
class Group:
    name: str
    lessons: List[int] # the index of the lesson

@dataclass
class Lesson:
    teacher: Teacher
    group: Group
    day: int
    hour: int

@dataclass
class Timetable:
    # subjects: List[Subject]
    lessons: List[Lesson]
    
    def countGapHours(self) -> int:
        """Couont all the gap hours in the timetable"""
        timetable = [[[]]]
        
        gap_hours = 0

        for lesson in self.lessons:
            d, h, g = lesson.day, lesson.hour, lesson.group

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
    
    def canSchedule(self, d, h, t, g) -> bool:
        """Check if this lesson is allowed to be scheduled"""
        for lesson in self.lessons:
            ds, hs, ts, gs = lesson.day, lesson.hour, lesson.teacher, lesson.group

            if (ds == d and hs == h) and (gs == g or ts == t):
                return False
        
        return True