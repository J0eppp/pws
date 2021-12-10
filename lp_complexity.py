import matplotlib.pyplot as plt
from solver.LPSolver import LPSolver
from solver.datatypes import Timetable, Lesson, Teacher, Group, SubjectInformation
from time import time


def main():
    # Kleine dataset
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(4)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(
        1, "Doc Eng 1", "Engels", []), Teacher(2, "Doc Wisk 1", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)


if __name__ == "__main__":
    main()
