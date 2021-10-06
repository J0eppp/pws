from ..parser import parse_json_file
from ..datatypes import Timetable


def test_timetable_schedule_lesson_1():
    # Test 1
    timetable: Timetable = parse_json_file(
        "solver/tests/test0.json")
    assert len(timetable.groups) == 1
    assert len(timetable.teachers) == 1
    assert timetable.create_feasible_timetable() == True
    assert len(timetable.lessons) == 1
    assert len(timetable.groups[0].lessons) == 1
    assert len(timetable.teachers[0].lessons) == 1


def test_timetable_schedule_lesson_2():
    # Test 2
    timetable: Timetable = parse_json_file("solver/tests/test1.json")
    assert len(timetable.groups) == 3
    assert len(timetable.teachers) == 3
    assert timetable.create_feasible_timetable() == True
    assert len(timetable.lessons) == 33
    for group in timetable.groups:
        assert len(group.lessons) == 11

    subject_info = {}

    for si in timetable.subject_information:
        subject_info[si.subject] = si.amount

    for teacher in timetable.teachers:
        assert len(
            teacher.lessons) == subject_info[teacher.subject] * len(timetable.groups)
