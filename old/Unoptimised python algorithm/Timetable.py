from tabulate import tabulate

from Subject import Subject
from Lesson import Lesson
from Group import Group
from Teacher import Teacher


class Timetable():
    def __init__(self, hours, groups, subjects, teachers):
        self.lessons = []
        self.hours = hours
        self.groups = groups
        self.subjects = subjects
        self.teacher = teachers

    def add_lesson(self, group: Group, subject: Subject, hour: int, *teacher: Teacher):
        lesson = Lesson(hour, group, subject)
        group.add_lesson(lesson)
        subject.add_lesson(lesson)
        self.lessons.append(lesson)
        pass

    def table(self):
        groups = [group.group for group in self.groups]
        data = [["", "", "", "", "", "", "", "", ""]
                for _ in range(len(self.hours))]
        for lesson in self.lessons:
            data[lesson.hour-1][groups.index(lesson.group.group)] = str(lesson)
        return tabulate(data, headers=groups)
