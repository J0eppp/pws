from ..parser import parse_json_file
from ..datatypes import Timetable, Lesson


def test_timetable_count_gap_hours():
    timetable: Timetable = parse_json_file("solver/tests/test1.json")
    lesson: Lesson = Lesson(len(timetable.lessons) - 1,
                            timetable.teachers[0], timetable.groups[0], 0, 0)
    assert timetable.schedule_lesson(lesson) == True
    lesson: Lesson = Lesson(len(timetable.lessons) - 1,
                            timetable.teachers[0], timetable.groups[0], 0, 2)
    group = timetable.groups[0]
    assert timetable.count_gap_hours() == 1
