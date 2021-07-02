#!/usr/bin/python3
from tabulate import tabulate


class Obj():
    def __init__(self):
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def has_lesson(self, hour):
        for lesson in self.lessons:
            if lesson.hour == hour:
                return True
        return False


class Group(Obj):
    def __init__(self, group):
        self.group = group
        Obj.__init__(self)

    def had_subject(self, subject: str):
        for lesson in self.lessons:
            if lesson.subject.subject == subject:
                return True
        return False


class Subject(Obj):
    def __init__(self, subject):
        self.subject = subject
        Obj.__init__(self)


class Lesson():
    def __init__(self, hour, group: Group, subject: Subject):
        self.hour = hour
        self.group = group
        self.subject = subject

    def __str__(self):
        return f"{self.hour % 8 if self.hour / 8 < 1 else (self.hour % 8) + 1}: {self.group.group}-{self.subject.subject}"


class Timetable():
    def __init__(self, hours, groups, subjects):
        self.lessons = []
        self.hours = hours
        self.groups = groups
        self.subjects = subjects

    def add_lesson(self, group: Group, subject: Subject, hour: int):
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


if __name__ == "__main__":
    groups = [Group("1A"), Group("1B"), Group("1C"), Group("1D"), Group(
        "1E"), Group("1F"), Group("1G"), Group("1H"), Group("1I")]
    subjects = [Subject("Nederlands"), Subject("Engels"), Subject("Wiskunde"), Subject("Geschiedenis"), Subject(
        "Aardrijkskunde"), Subject("Biologie"), Subject("Frans"), Subject("LO"), Subject("BV"), Subject("Drama"), Subject("Muziek")]
    # hours = [1, 2, 3, 4, 5, 6, 7, 8]
    hours = list(range(1, 41))
    timetable = Timetable(hours, groups, subjects)

    def algorithm():
        for subject in subjects:
            for group in groups:
                for hour in hours:
                    # Check if the subject is already given at this hour
                    if subject.has_lesson(hour) == True:
                        continue  # check next hour
                    # Check if the group has a lesson this hour
                    if group.has_lesson(hour) == True:
                        continue  # check next hour
                    # Check if the group has already had this lesson
                    if group.had_subject(subject.subject) == True:
                        break  # check next group
                    timetable.add_lesson(group, subject, hour)

    algorithm()

    print(timetable.table())
