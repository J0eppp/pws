from typing import List
from dataclasses import dataclass

@dataclass
class BaseType:
    identifier: int

@dataclass
class Teacher(BaseType):
    name: str
    subject: str

@dataclass
class Group(BaseType):
    name: str
    year: int
    subjects: List[str]
    lessons: List[int]

@dataclass
class Lesson(BaseType):
    teacher: Teacher
    group: Group
    hour: int
    day: int

@dataclass
class SubjectInformation:
    subject: str
    year: int
    amount: int

class Timetable:
    """This class will contain all data and methods to create a feasible timetable, to give to the LP"""
    def __init__(self, groups: List[Group], teachers: List[Teacher], subject_information: List[SubjectInformation]):
        self.groups: List[Group] = groups
        self.teachers: List[Teacher] = teachers
        self.subject_information: List[SubjectInformation] = subject_information
