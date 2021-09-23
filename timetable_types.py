from enum import Enum, auto
from dataclasses import dataclass
from typing import List

# Enum with all subjects
class Subject(Enum):
    NEDERLANDS = auto()
    WISKUNDE = auto()
    ENGELS = auto()
    NASK = auto()
    GESCHIEDENIS = auto()
    BIOLOGIE = auto()
    AARDRIJKSKUNDE = auto()
    FRANS = auto()
    DUITS = auto()

@dataclass
class Timetable:
    subjects: List[Subject]

