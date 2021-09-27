from enum import Enum, auto
from dataclasses import dataclass
from typing import List
from GapCounter import countGapHours

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

@dataclass
class Timetable:
    # subjects: List[Subject]
    lessons: List[Lesson]

@dataclass
class GapHours:
    amount: countGapHours