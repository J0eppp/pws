from solver.parser import parse_json_file
from solver.datatypes import Timetable, Lesson


def test_timetable_can_schedule_lesson_1():
    timetable: Timetable = parse_json_file("tests/test1.json")
    lesson: Lesson = Lesson(len(timetable.lessons) - 1,
                            timetable.teachers[0], timetable.groups[0], 0, 0)
    assert timetable.can_schedule(lesson) == True
    assert timetable.schedule_lesson(lesson) == True
    assert timetable.can_schedule(lesson) == False

    lesson: Lesson = Lesson(len(timetable.lessons) - 1,
                            timetable.teachers[0], timetable.groups[0], 1, 0)
    assert timetable.can_schedule(lesson) == True
    assert timetable.schedule_lesson(lesson) == True
    assert timetable.can_schedule(lesson) == False
