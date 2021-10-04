from typing import List
from dataclasses import dataclass


@dataclass
class BaseType:
    identifier: int


@dataclass
class Teacher(BaseType):
    name: str
    subject: str
    lessons: List[int]


@dataclass
class Group(BaseType):
    name: str
    year: int
    subjects: List[str]
    lessons: List["Lesson"]

    def count_gap_hours(self, amount_days_in_a_week: int) -> int:
        timetable = [[]] * amount_of_days_in_a_week

        for lesson in self.lessons:
            timetable[lesson.day].append(lesson.hour)
        
        amount = 0
        for day in timetable:
            if day == None:
                continue
            
            day.sort()
            first = day[0]
            last = day[-1]
            amount += last - (first - 1) - len(day)

        return amount



@dataclass
class Lesson(BaseType):
    teacher: Teacher
    group: Group
    hour: int
    day: int

    def __str__(self) -> str:
        return f"D{self.day}H{self.hour} - G {self.group.name} T {self.teacher.name}"


@dataclass
class SubjectInformation:
    subject: str
    year: int
    amount: int


@dataclass
class Timetable:
    """This class will contain all data and methods to create a feasible timetable, to give to the LP"""
    groups: List[Group]
    teachers: List[Teacher]
    subject_information: List[SubjectInformation]
    amount_of_days_a_week: int
    amount_of_hours_a_day: int
    lessons: List[Lesson]

    def can_schedule(self, lesson: Lesson) -> bool:
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
        self.lessons.append(lesson)
        for group in self.groups:
            if group.identifier == lesson.group.identifier:
                group.lessons.append(lesson)

        for teacher in self.teachers:
            if teacher.identifier == lesson.teacher.identifier:
                teacher.lessons.append(lesson)

        return True

    def count_gap_hours(self) -> int:
        """Count all the gap hours in the timetable"""
        gap_hours = 0

        for group in self.groups:
            gap_hours += group.count_gap_hours(self.amount_of_days_a_week)

        # lessons_by_group = dict(
        #     (group.name, [[]] * self.amount_of_days_a_week) for group in self.groups)

        # print(lessons_by_group)

        # for lesson in self.lessons:
        #     print(lesson.day)
        #     lessons_by_group[lesson.group.name][lesson.day].append(lesson)

        # for i in lessons_by_group:
        #     for j in range(len(lessons_by_group[i])):
        #         print(len(lessons_by_group[i][j]))

        # for group in lessons_by_group:
        #     for day in range(len(lessons_by_group[group])):
        #         arr = lessons_by_group[group][day]
        #         # print(f"Day: {day} len: {len(arr)}")
        #         if arr == None:
        #             continue
        #         arr.sort(key=lambda x: x.hour)
        #         # print([str(x) for x in arr])
        #         for lesson in arr:
        #             print(lesson)

        return gap_hours

    # def count_gap_hours(self) -> int:
    #     """Count all the gap hours in the timebale"""
    #     gap_hours = 0

    #     timetable = dict((lesson.group.name, [
    #                      []] * self.amount_of_days_a_week) for lesson in self.lessons)
    #     print(timetable)
    #     for lesson in self.lessons:
    #         print("Lesson day: ", lesson.day)
    #         timetable[lesson.group.name][lesson.day].append(lesson)

    #     for group in timetable:
    #         print(group)
    #         for day in timetable[group]:
    #             # for lesson in timetable[group][day]:
    #             for lesson in day:
    #                 print(lesson.teacher.name, lesson.group.name,
    #                       lesson.day, lesson.hour)

    #     counter = 0

    #     for group in timetable:
    #         # for day in range(self.amount_of_days_a_week):
    #         for day in timetable[group]:
    #             counter += 1
    #             # timetable[group][day].sort(key=lambda x: x.hour)
    #             # arr = timetable[group][day]
    #             arr = sorted(day, key=lambda x: x.hour)
    #             first = arr[0]
    #             last = arr[-1]
    #             print("Day: ", day[0].day)
    #             print(first.hour)
    #             print(last.hour)
    #             amount = last.hour - (first.hour - 1) - len(arr)
    #             gap_hours += amount

    #     print("Counter: ", counter)

    #     return gap_hours
