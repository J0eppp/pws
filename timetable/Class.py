from Default import Default


class Class(Default):
    """
    A class contains a subject, teacher and group

    @param subject [Subject] The name/id of the subject
    @param teacher [Teacher] The teacher that teaches the subject
    @param group [Group] The group that is being teached
    """

    def __init__(self, subject=None teacher=None, group=None):
        self.subject = subject
        self.teacher = teacher
        self.group = group
