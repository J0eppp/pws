from Default import Default


class Teacher(Default):
    """
    The teacher representation

    @property classes [Class[]] All the teacher's classes
    """

    def __init__(self):
        Default.__init__(self)
        self.classes = []


if __name__ == "__main__":
    teacher = Teacher()
    print(teacher.json())
