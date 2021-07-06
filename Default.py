class Default():
    def __init__(self):
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def has_lesson(self, hour):
        for lesson in self.lessons:
            if lesson.hour == hour:
                return True
        return False
