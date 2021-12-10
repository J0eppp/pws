# import matplotlib.pyplot as plt
from solver.LPSolver import LPSolver
from solver.datatypes import Timetable, Teacher, Group, SubjectInformation
from time import time
# from sklearn.linear_model import LinearRegression

# from sklearn.linear_model import Perceptron
# from sklearn.preprocessing import PolynomialFeatures
# import numpy as np

from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series
from openpyxl.chart.trendline import Trendline


def main():
    workbook = Workbook()
    worksheet = workbook.active

    chart = ScatterChart()
    chart.x_axis.title = "Invoer (n)"
    chart.y_axis.title = "Tijd (s)"
    chart.title = "Complexiteit LP algoritme"

    x = []
    y = []

    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    
    teachers = []
    
    # Create the teachers
    for subject in subject_information:
        for i in range(5):
            teachers.append(Teacher(len(teachers), f"Docent {subject.subject} {i + 1}", subject.subject, []))
    
    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
    
    for i in range(10):
        groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
              for i in range(4 * (i + 1))]
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

        for group in groups:
            group.lessons = []
        for teacher in teachers:
            teacher.lessons = []

    # # Dataset 1
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(4)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    # # Dataset 2
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(8)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    # # Dataset 3
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(12)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    # # Dataset 4
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(16)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    # # Dataset 5
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(20)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    # # Dataset 6
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(24)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    # # Dataset 7
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(28)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    # # Dataset 8
    # groups = [Group(i, str(i), 1, ["Nederlands", "Engels", "Wiskunde"], [])
    #           for i in range(32)]
    # teachers = [Teacher(0, "Doc Ned 1", "Nederlands", []), Teacher(1, "Doc Ned 2", "Nederlands", []), Teacher(2, "Doc Eng 1", "Engels", [
    # ]), Teacher(3, "Doc Eng 2", "Engels", []), Teacher(4, "Doc Wisk 1", "Wiskunde", []), Teacher(5, "Doc Wisk 2", "Wiskunde", [])]
    # subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
    #     "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]
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

    print(x)
    print(y)

    worksheet.append(["x", "y"])

    for i in range(len(x)):
        worksheet.append([x[i], y[i]])

    xvalues = Reference(worksheet, min_col=1, min_row=2, max_row=len(x) + 1)

    for i in range(2, 3):
        values = Reference(worksheet, min_col=i, min_row=1, max_row=len(x) + 1)
        series = Series(values, xvalues)
        series.trendline = Trendline(dispRSqr=True, dispEq=True, trendlineType="poly")
        chart.series.append(series)

    # trendline = Trendline(dispRSqr=True, dispEq=True, trendlineType="poly")
    # chart.series[0].trendline = trendline
    
    worksheet.add_chart(chart, "D10")

    workbook.save("lp_complexity.xlsx")

    # plt.scatter(x, y)

    # plt.show()


if __name__ == "__main__":
    main()
