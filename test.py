import unittest

from Default import Default
from Lesson import Lesson
from Group import Group
from Subject import Subject


class Test(unittest.TestCase):
    def test_Default_has_lesson(self):
        d = Default()
        l = Lesson(1, None, None)
        d.add_lesson(l)
        self.assertTrue(d.has_lesson(1))

    def test_Group_had_subject(self):
        g = Group("test")
        l = Lesson(1, g, Subject("Nederlands", 1))
        g.add_lesson(l)
        self.assertTrue(g.had_subject("Nederlands"))


if __name__ == '__main__':
    unittest.main()
