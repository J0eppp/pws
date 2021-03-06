from typing import List, Any
from dataclasses import dataclass
from . import utils
from mip import xsum

import json


@dataclass
class BaseType:
    identifier: int


@dataclass
class Teacher(BaseType):
    name: str
    subject: str
    lessons: List["Lesson"]
    selected_amount: int = 0

    def __str__(self) -> str:
        return f"{self.name}, subject: {self.subject}"

    def select_lessons(self):
        self.lessons = [
            lesson for lesson in self.lessons if lesson.scheduled.x >= 0.99]

    @property
    def json(self):
        return {"name": self.name, "subject": self.subject}


@dataclass
class Group(BaseType):
    name: str
    year: int
    subjects: List[str]
    lessons: List["Lesson"]

    def __str__(self) -> str:
        return f"{self.name}"

    def count_gap_hours(self, amount_of_days_in_a_week: int, amount_of_hours_a_day: int) -> int:
        # Create a 2D list so we can save all the days and hours the group has a lesson
        timetable = [[] for _ in range(amount_of_days_in_a_week)]

        amounts = []

        for day in range(amount_of_days_in_a_week):
            for hour in range(amount_of_hours_a_day):
                lessons = self.get_lessons(hour)
                timetable[day].append([lesson.scheduled for lesson in lessons])

            first = 0
            last = 0

            for i in range(len(timetable[day]) - 1, 0, -1):
                hour: List["Lesson"] = timetable[day][i]
                # We check if first > i and then if there is a lesson scheduled on this hour
                if first > i and xsum(hour) * i != 0:
                    first = i

            for i in range(len(timetable[day])):
                hour: List["Lesson"] = timetable[day][i]
                # We check first if last < i and then if there is a lesson scheduled on this hour
                # utils.uprint(xsum(hour) >= 0.99)
                if last < i and xsum(hour) * i != 0:
                    last = i

            # utils.uprint(f"First: {first}")
            # utils.uprint(f"Last: {last}")

            amounts.append(last - (first - 1) -
                           xsum([lesson.scheduled for lesson in lessons]))

        return xsum(amounts)

    def get_lessons(self, hour) -> List["Lesson"]:
        return [lesson for lesson in self.lessons if lesson.hour == hour]

    def select_lessons(self):
        self.lessons = [
            lesson for lesson in self.lessons if lesson.scheduled.x >= 0.99]

    @property
    def json(self):
        return {"name": self.name, "year": self.year, "subjects": self.subjects}


@dataclass
class Lesson(BaseType):
    """Represents a lesson"""
    teacher: Teacher
    group: Group
    day: int
    hour: int
    subj_info: 'SubjectInformation'
    scheduled: Any

    def __str__(self) -> str:
        return f"D{self.day + 1}H{self.hour + 1} - {self.group.name} - {self.teacher.subject} - {self.teacher.name}"

    @property
    def json(self) -> str:
        return {"day": self.day, "hour": self.hour, "teacher": self.teacher.json, "group": self.group.json, "subjectInfo": self.subj_info.json, "scheduled": self.scheduled.x}

    def excel_str(self) -> str:
        return f"D{self.day + 1}H{self.hour + 1} - {self.teacher.subject} ({self.teacher.name})"


@dataclass
class SubjectInformation:
    subject: str
    year: int
    amount: int

    @property
    def json(self):
        return {"subject": self.subject, "year": self.year, "amount": self.amount}


@dataclass
class Timetable:
    """This class contains all the data and methods to represent a timetable"""
    groups: List[Group]
    teachers: List[Teacher]
    subject_information: List[SubjectInformation]
    amount_of_days_a_week: int
    amount_of_hours_a_day: int
    lessons: List[Lesson]

    def can_schedule(self, lesson: Lesson) -> bool:
        """Check if the lesson can be scheduled"""
        # First we check if we can schedule this for the group
        # Loop through all the lessons for the group
        for l in lesson.group.lessons:
            # Check if there is a lesson at the same time as the lesson we want to schedule
            if l.day == lesson.day and l.hour == lesson.hour:
                # There is, return false
                return False

        # Then we check if we can schedule this for the teacher
        # Loop through all the lessons for the teacher
        for l in lesson.teacher.lessons:
            # Check if there is a lesson at the same time as the lesson we want to schedule
            if l.day == lesson.day and l.hour == lesson.hour:
                # There is, return false
                return False

        # Everything is fine, return true
        return True

    def schedule_lesson(self, lesson: Lesson, skip_check=False) -> bool:
        # First we check if we are allowed to schedule this lesson
        if skip_check == False:
            if self.can_schedule(lesson) == False:
                return False

        # Then we schedule the lesson
        utils.uprint(f"Scheduling: {lesson}")
        self.lessons.append(lesson)

        # Then we add it to the group's lessons list
        for group in self.groups:
            # Find the group
            if group.identifier == lesson.group.identifier:
                group.lessons.append(lesson)

        # Then we add it to the teacher's lessons list
        for teacher in self.teachers:
            # Find the teacher
            if teacher.identifier == lesson.teacher.identifier:
                teacher.lessons.append(lesson)
                break

        return True

    def count_gap_hours(self) -> int:
        """Count all the gap hours in the timetable"""
        gap_hours = 0

        # Loop through all the groups and count their gap hours
        # for group in self.groups:
        #     gap_hours += group.count_gap_hours(self.amount_of_days_a_week)

        return xsum([group.count_gap_hours(self.amount_of_days_a_week) for group in self.groups])

    def create_feasible_timetable(self, add_var, BINARY) -> bool:
        """Create a valid timetable"""
        self.lessons = []  # empty the lessons, to be sure
        for group in self.groups:
            for subject in group.subjects:
                amount = 0
                scheduled = 0
                si = None
                for subject_info in self.subject_information:
                    if subject_info.subject == subject and subject_info.year == group.year:
                        amount = subject_info.amount
                        si = subject_info
                        break
                teacher = None
                for t in self.teachers:
                    if t.subject == subject:
                        teacher = t
                        break

                for _ in range(amount):
                    if scheduled == amount:
                        break
                    for day in range(self.amount_of_days_a_week):
                        if scheduled == amount:
                            break
                        for hour in range(self.amount_of_hours_a_day):
                            if scheduled == amount:
                                break
                            lesson = Lesson(
                                len(self.lessons) - 1, teacher, group, day, hour, si, add_var(var_type=BINARY))
                            if self.schedule_lesson(lesson) == True:
                                scheduled += 1

                if scheduled != amount:
                    utils.uprint(
                        f"[ERROR] could not schedule all lessons for subject: {subject}, group: name: {group.name}, year: {group.year}, id: {group.identifier}")
                    return False

        return True

    @property
    def json(self):
        return {"lessons": [lesson.json for lesson in self.lessons]}
