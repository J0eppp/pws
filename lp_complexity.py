import matplotlib.pyplot as plt
from solver.LPSolver import LPSolver
from solver.datatypes import Timetable, Teacher, Group, SubjectInformation
from time import time
from sklearn.linear_model import LinearRegression

from sklearn.linear_model import Perceptron
from sklearn.preprocessing import PolynomialFeatures
import numpy as np


def main():
    x = []
    y = []

    # Dataset 1
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(4)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # Dataset 2
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(8)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # Dataset 3
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(12)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # Dataset 4
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(16)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # Dataset 5
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(20)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # Dataset 6
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(24)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # Dataset 7
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(28)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # Dataset 8
    groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(32)]
    teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    timetable: Timetable = Timetable(
        groups, teachers, subject_information, 5, 9, [])
    solver = LPSolver(timetable)
    start_time = time()
    solver.solve()
    end_time = time()
    time_diff = end_time - start_time
    amount_of_vars = solver.model.num_cols
    x.append(amount_of_vars)
    y.append(time_diff)

    # # Dataset 6
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(20)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 4), SubjectInformation(
    #     "Engels", 1, 4), SubjectInformation("Wiskunde", 1, 4)]
    # timetable: Timetable = Timetable(
    #     groups, teachers, subject_information, 5, 9, [])
    # solver = LPSolver(timetable)
    # start_time = time()
    # solver.solve()
    # end_time = time()
    # time_diff = end_time - start_time
    # amount_of_vars = solver.model.num_cols
    # x.append(amount_of_vars)
    # y.append(time_diff)

    # regressielijn = LinearRegression()
    # regressielijn.polyfit([[i] for i in x], [[i] for i in y])

    # X = PolynomialFeatures(interaction_only=True).fit_transform(
    #     [[i] for i in x]).astype(int)
    # clf = Perceptron(fit_intercept=False, max_iter=10,
    #                  tol=None, shuffle=False).fit(X, [[i] for i in y])

    # plt.plot([[i] for i in x], clf.predict(X))

    print(x)
    print(y)

    plt.scatter(x, y)

    plt.show()


if __name__ == "__main__":
    main()
