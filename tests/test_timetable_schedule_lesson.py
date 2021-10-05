import solver
from solver.parser import parse_json_file
from solver.datatypes import Timetable


def test_timetable_schedule_lesson():
    timetable: Timetable = parse_json_file(
        "tests/test0.json")
    print(timetable)
    assert len(timetable.groups) == 1
