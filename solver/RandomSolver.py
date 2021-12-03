from .Solver import Solver
from .datatypes import Timetable, Lesson
from . import utils

import time

SEPERATION_STRING = "-==================================-"


class RandomSolver(Solver):
    def __init__(self, timetable: Timetable, verbosity: int = 0):
        self.timetable = timetable
        self.verbosity = verbosity

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        start_time = 0
        end_time = 0
        if self.verbosity == 1:
            utils.uprint(SEPERATION_STRING)
            utils.uprint("Starting the random solver")
            utils.uprint(SEPERATION_STRING)

            utils.uprint(SEPERATION_STRING)
            utils.uprint("Creating all lessons")
            start_time = time.time()

        timetable = self.timetable
        for group in timetable.groups:
            for subj in group.subjects:
                subject = None
                for si in timetable.subject_information:
                    if si.subject == subj:
                        subject = si
                        break

                # We have the subject information
                amount_scheduled = 0
                # Find a teacher
                teacher = sorted([teacher for teacher in self.timetable.teachers if teacher.subject == subj],
                                 key=lambda x: x.selected_amount)[0]
                teacher.selected_amount += 1
                for _ in range(subject.amount):
                    if amount_scheduled == subject.amount:
                        break

                    for day in range(timetable.amount_of_days_a_week):
                        if amount_scheduled == subject.amount:
                            break
                        for hour in range(timetable.amount_of_hours_a_day):
                            if amount_scheduled == subject.amount:
                                break
                            lesson = Lesson(
                                len(timetable.lessons), teacher, group, day, hour, subject, 1)
                            if timetable.schedule_lesson(lesson) == True:
                                amount_scheduled += 1

        # for group in self.timetable.groups:
        #     found_subject = False
        #     for subject in group.subjects:
        #         if found_subject == True:
        #             break
        #         for si in self.timetable.subject_information:
        #             if found_subject == True:
        #                 break
        #             if si.subject != subject and si.year != group.year:
        #                 continue
        #             found_subject = True
        #             teacher = sorted([teacher for teacher in self.timetable.teachers if teacher.subject == subject],
        #                              key=lambda x: x.selected_amount)[0]
        #             teacher.selected_amount += 1
        #             for _ in range(si.amount):
        #                 selected = False
        #                 for day in range(self.timetable.amount_of_days_a_week):
        #                     if selected == True:
        #                         break
        #                     for hour in range(self.timetable.amount_of_hours_a_day):
        #                         lesson = Lesson(
        #                             len(self.timetable.lessons), teacher, group, day, hour, si, 0)
        #                         if self.timetable.schedule_lesson(lesson) == True:
        #                             selected = True
        #                             break

        if self.verbosity == 1:
            end_time = time.time()
            utils.uprint("Done creating all lessons")
            utils.uprint(
                f"Created {len(self.timetable.lessons)} lessons in {end_time - start_time}")
            utils.uprint(SEPERATION_STRING)

        return self.timetable
