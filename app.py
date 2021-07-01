data = {
    "groups": ["A", "B", "C"],
    "hours": [1, 2, 3, 4],
    "subjects": ["α", "β", "γ"]
}


class Lesson():
    def __init__(self, hour, group, subject):
        self.hour = hour
        self.group = group
        self.subject = subject

    def bezet(self):
        return self.subject != None and self.group != None

    def set(self, hour, group, subject):
        self.hour = hour
        self.group = group
        self.subject = subject

    def __str__(self):
        if self.bezet() == True:
            return f"Klas: {self.group}, uur: {self.hour}, vak: {self.subject}"
        return ""


timetable = {
    "A": [Lesson(0, "A", None)] * 4,
    "B": [Lesson(0, "B", None)] * 4,
    "C": [Lesson(0, "C", None)] * 4,
}

subjects = {
    "α": [Lesson(1, None, "α"), Lesson(2, None, "α"), Lesson(3, None, "α"), Lesson(4, None, "α")],
    "β": [Lesson(1, None, "β"), Lesson(2, None, "β"), Lesson(3, None, "β"), Lesson(4, None, "β")],
    "γ": [Lesson(1, None, "γ"), Lesson(2, None, "γ"), Lesson(3, None, "γ"), Lesson(4, None, "γ")],
}

for s in range(len(data["subjects"])):
    for g in range(len(data["groups"])):
        for h in range(len(data["hours"])):
            print(timetable[data["groups"][g]][data["hours"][h] - 1].bezet())
            if timetable[data["groups"][g]][data["hours"][h] - 1].bezet() == True or subjects[data["subjects"][s]][data["hours"][h] - 1].bezet() == True:
                continue
            timetable[data["groups"][g]][h].set(
                data["hours"][h], data["groups"][s], data["subjects"][s])
            subjects[data["subjects"][s]][data["hours"][h] -
                                          1].set(data["hours"][h], data["groups"][s], data["subjects"][s])


for t in timetable:
    for l in timetable[t]:
        print(l)

for s in subjects:
    for l in subjects[s]:
        print(l)
