# from ..parser import parse_json_file
# from ..datatypes import Timetable, Lesson


# def test_timetable_count_gap_hours():
#     timetable: Timetable = parse_json_file("solver/tests/test1.json")
#     lesson: Lesson = Lesson(len(timetable.lessons) - 1,
#                             timetable.teachers[0], timetable.groups[0], 0, 0, None, None)
#     assert timetable.schedule_lesson(lesson) == True
#     lesson: Lesson = Lesson(len(timetable.lessons) - 1,
#                             timetable.teachers[0], timetable.groups[0], 0, 2, None, None)
#     assert timetable.schedule_lesson(lesson) == True
#     print([str(lesson) for lesson in timetable.lessons])
#     assert timetable.count_gap_hours() == 1
