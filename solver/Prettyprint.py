from solver.utils import uprint
from .datatypes import Timetable, Lesson, Group, Teacher

SEPERATION_STRING = "-==================================-"


def pretty_print(timetable: Timetable) -> str:

    for group in timetable.groups:
        daylist = [[] for _ in range(5)]
        print(f"Group {group.identifier}\n")
        for lesson in group.lessons:
            print(lesson.day)
            daylist[lesson.day].append(lesson)

        for i, day in enumerate(daylist):
            print(f"Day {i}")
            day.sort(key=lambda x: x.hour)
            [print(lesson) for lesson in day]

        print("\n")
        uprint(SEPERATION_STRING)
        print("\n")
