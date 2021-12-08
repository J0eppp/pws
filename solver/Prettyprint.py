from solver.utils import uprint
from .datatypes import Timetable, Lesson, Group, Teacher

SEPERATION_STRING = "-==================================-"


def pretty_print(timetable: Timetable) -> str:

    for group in timetable.groups:
        daylist = [[] for _ in range(5)]
        print(f"Group {group.identifier}\n")
        for lesson in group.lessons:
            daylist[lesson.day].append(lesson)

        for i, day in enumerate(daylist):
            print(f"Day {i + 1}")
            day.sort(key=lambda x: x.hour)
            [print(lesson) for lesson in day]

        uprint(SEPERATION_STRING)
