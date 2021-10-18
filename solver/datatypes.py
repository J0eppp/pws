from typing import List, Any
from dataclasses import dataclass
from . import utils
from mip import xsum
# import utils


@dataclass
class BaseType:
    identifier: int


@dataclass
class Teacher(BaseType):
    name: str
    subject: str
    lessons: List["Lesson"]

    def __str__(self) -> str:
        return f"{self.name}, subject: {self.subject}"

    def select_lessons(self):
        self.lessons = [lesson for lesson in self.lessons if lesson.scheduled.x >= 0.99]


@dataclass
class Group(BaseType):
    name: str
    year: int
    subjects: List[str]
    lessons: List["Lesson"]

    def __str__(self) -> str:
        return f"{self.name}"

    def count_gap_hours(self, amount_of_days_in_a_week: int) -> int:
        # Create a 2D list so we can save all the days and hours the group has a lesson
        # timetable = [[]] * amount_of_days_in_a_week

        penalty = {
            0 : 0,
            1 : 1,
            2 : 1,
            3 : 4,
            4 : 4,
            5 : 3,
            6 : 1,
            7 : 1,
            8 : 0,
        }
        timetable = [[] for _ in range(amount_of_days_in_a_week)]

        # Loop through each lesson and save it into the array
        for lesson in self.lessons:
            timetable[lesson.day].append(lesson)

        # Loop through each day and check how many gap hours there are in that day
        amounts = []
        for day in timetable:
            # Nothing there
            if day == None or len(day) == 0:
                continue

            # Only use the hours with scheduled >= 0.99
            amounts.append(xsum([(1 - lesson.scheduled) * penalty[lesson.hour] for lesson in day]))
            #amounts.append(8 - xsum([lesson.scheduled for lesson in day]))
            #[print(lesson.scheduled.ub) for lesson in day]
            # [print(lesson.scheduled) for lesson in day]
            # #print(len(selected_day))

            # # Sort the array so we can use it
            # selected_day.sort(key=lambda x: x.hour)
            # first = selected_day[0].hour
            # last = selected_day[-1].hour
            # # Calculate the amount of gap hours
            # amounts.append(last - (first - 1) - len(selected_day))
            #[print(amount) for amount in amounts]
        #print(xsum(amounts))
        return xsum(amounts)
    
    def select_lessons(self):
        self.lessons = [lesson for lesson in self.lessons if lesson.scheduled.x >= 0.99]


@dataclass
class Lesson(BaseType):
    teacher: Teacher
    group: Group
    day: int
    hour: int
    subj_info: 'SubjectInformation'
    scheduled: Any


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
                            lesson = Lesson(
                                len(self.lessons) - 1, teacher, group, day, hour, add_var(var_type=BINARY))
                            if self.schedule_lesson(lesson) == True:
                                scheduled += 1

                if scheduled != amount:
                    utils.uprint(
                        f"[ERROR] could not schedule all lessons for subject: {subject}, group: name: {group.name}, year: {group.year}, id: {group.identifier}")
                    return False

        return True
