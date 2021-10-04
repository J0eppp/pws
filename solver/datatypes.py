from typing import List
from dataclasses import dataclass
import utils


@dataclass
class BaseType:
    identifier: int


@dataclass
class Teacher(BaseType):
    name: str
    subject: str
    lessons: List["Lesson"]


@dataclass
class Group(BaseType):
    name: str
    year: int
    subjects: List[str]
    lessons: List["Lesson"]

    def count_gap_hours(self, amount_of_days_in_a_week: int) -> int:
        timetable = [[]] * amount_of_days_in_a_week

        for lesson in self.lessons:
            timetable[lesson.day].append(lesson.hour)
        
        amount = 0
        for day in timetable:
            if day == None or len(day) == 0:
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
        return f"D{self.day}H{self.hour} - G {self.group.name} T {self.teacher.name} subject {self.teacher.subject}"


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
        utils.uprint(f"Scheduling: {lesson}")
        if skip_check == False:
            if self.can_schedule(lesson) == False:
                return False

        # Then we schedule the lesson
        self.lessons.append(lesson)

        # Then we add it to the group's lessons list
        for group in self.groups:
            if group.identifier == lesson.group.identifier:
                group.lessons.append(lesson)

        # Then we add it to the teacher's lessons list
        for teacher in self.teachers:
            if teacher.identifier == lesson.teacher.identifier:
                teacher.lessons.append(lesson)

        return True

    def count_gap_hours(self) -> int:
        """Count all the gap hours in the timetable"""
        gap_hours = 0

        for group in self.groups:
            gap_hours += group.count_gap_hours(self.amount_of_days_a_week)

        return gap_hours
    
    def create_feasible_timetable(self) -> bool:
        """Create a valid timetable"""
        lessons = []
        for group in self.groups:
            for subject in group.subjects:
                amount = 0
                scheduled = 0
                for subject_info in self.subject_information:
                    if subject_info.subject == subject and subject_info.year == group.year:
                        amount = subject_info.amount
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
                            lesson = Lesson(len(self.lessons) - 1, t, group, hour, day)
                            if self.schedule_lesson(lesson) == True:
                                lessons.append(lesson)
                                scheduled += 1
                
                if scheduled != amount:
                    utils.uprint(f"[ERROR] could not schedule all lessons for subject: {subject}, group: name: {group.name}, year: {group.year}, id: {group.identifier}")
                    return False
                
        self.lessons = lessons
        return True