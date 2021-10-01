#!/usr/bin/python3
from Group import Group
from Subject import Subject
from Timetable import Timetable

from time import perf_counter


if __name__ == "__main__":
    t = perf_counter()
    groups = [Group("1A"), Group("1B"), Group("1C"), Group("1D"), Group(
        "1E"), Group("1F"), Group("1G"), Group("1H"), Group("1I")]
    subjects = [Subject("Nederlands", 1), Subject("Engels", 1), Subject("Wiskunde", 1), Subject("Geschiedenis", 1), Subject(
        "Aardrijkskunde", 1), Subject("Biologie", 1), Subject("Frans", 1), Subject("LO", 1), Subject("BV", 1), Subject("Drama", 1), Subject("Muziek", 1)]
    # hours = [1, 2, 3, 4, 5, 6, 7, 8]
    hours = list(range(1, 41))
    teachers = []
    timetable = Timetable(hours, groups, subjects, teachers)

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
    print(f"Code execution took {perf_counter() - t:0.4f} seconds")
