from solver.LPSolver import LPSolver
from solver.datatypes import Timetable, Teacher, Group, SubjectInformation
from time import time

from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series


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
            teachers.append(Teacher(
                len(teachers), f"Docent {subject.subject} {i + 1}", subject.subject, []))

    subject_information = [SubjectInformation("Nederlands", 1, 2), SubjectInformation(
        "Engels", 1, 2), SubjectInformation("Wiskunde", 1, 2)]

    for i in range(3):
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

    print(x)
    print(y)

    worksheet.append(["x", "y"])

    for i in range(len(x)):
        worksheet.append([x[i], y[i]])

    xvalues = Reference(worksheet, min_col=1, min_row=2, max_row=len(x) + 1)

    for i in range(2, 3):
        values = Reference(worksheet, min_col=i, min_row=1, max_row=len(x) + 1)
        series = Series(values, xvalues)
        chart.series.append(series)

    worksheet.add_chart(chart, "D10")

    workbook.save("lp_complexity.xlsx")


if __name__ == "__main__":
    main()
