from Default import Default

class Group(Default):
    def __init__(self, group):
        self.group = group
        Default.__init__(self)

    def had_subject(self, subject: str):
        for lesson in self.lessons:
            if lesson.subject.subject == subject:
                return True
        return False