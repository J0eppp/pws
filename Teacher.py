from Default import Default


# Teacher class contains data about teachers (what subjects they can teach, their availability, etc) and has methods to e.g. check if they already have a lesson during a specific hour
class Teacher(Default):
    def __init__(self, subjects):
        Default.__init__(self)
        self.subjects = subjects
