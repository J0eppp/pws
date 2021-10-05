import json
from .datatypes import Timetable, Group, Teacher, SubjectInformation


def parse_json_file(path: str) -> Timetable:
    file = None
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print("Could not find the file")
        return None

    data = json.load(file)
    file.close()
    groups = None
    teachers = None
    subject_information = None
    amount_of_days_a_week = None
    amount_of_hours_a_day = None
    lessons = None

    try:
        groups = data["groups"]
        teachers = data["teachers"]
        subject_information = data["subjectInformation"]
        amount_of_days_a_week = data["amountOfDaysAWeek"]
        amount_of_hours_a_day = data["amountOfHoursADay"]
        lessons = data["lessons"]
    except KeyError as e:
        print(f"Invalid file, property {str(e)} was not found")
        return None

    data_subject_information = []
    for si in subject_information:
        t = SubjectInformation(si["subject"], si["year"], si["amount"])
        data_subject_information.append(t)

    data_groups = []
    for i in range(len(groups)):
        group = groups[i]
        t = Group(i, group["name"], group["year"],
                  group["subjects"], group["lessons"])
        data_groups.append(t)

    data_teachers = []
    for i in range(len(teachers)):
        teacher = teachers[i]
        t = Teacher(i, teacher["name"], teacher["subject"], teacher["lessons"])
        data_teachers.append(t)

    timetable = Timetable(data_groups, data_teachers, data_subject_information, int(
        amount_of_days_a_week), int(amount_of_hours_a_day), lessons)

    return timetable
