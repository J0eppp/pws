from Group import Group
from Subject import Subject

class Lesson():
    def __init__(self, hour, group: Group, subject: Subject):
        self.hour = hour
        self.group = group
        self.subject = subject

    def __str__(self):
        return f"{self.hour % 8 if self.hour / 8 < 1 else (self.hour % 8) + 1}: {self.group.group}-{self.subject.subject}"
