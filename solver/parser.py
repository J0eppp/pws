import json
from datatypes import Timetable, Group, Teacher, SubjectInformation

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

    try:
        groups = data["groups"]
        teachers = data["teachers"]
        subject_information = data["subjectInformation"]
    except KeyError as e:
        print(f"Invalid file, property {str(e)} was not found")
        return None
    
    timetable = Timetable([], [], [])
    
    temp = []
    for si in subject_information:
        t = SubjectInformation(si.subject, si.year, si.amount)
        temp.append(t)
    timetable.subject_information = temp

    temp = []
    for i in range(len(groups)):
        group = groups[i]
        t = Group(i, group.name, group.year, group.subjects, group.lessons)
    timetable.groups = temp

    temp = []
    for i in range(len(teachers)):
        teacher = teachers[i]
        t = Teacher(i, teacher.name, teacher.subject)
    timetable.teachers = temp

    return Timetable