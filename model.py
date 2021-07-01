groups = ["A", "B", "C"]
hours = [1, 2, 3, 4]
# subjects = ["α", "β", "γ"]


# class Group():
#     def __init__(self, name: str):
#         self.name = name
#         self.timetable = [None] * 4


subjects = {
    "α": [None] * len(hours),
    "β": [None] * len(hours),
    "γ": [None] * len(hours),
}


for subject in subjects:
    for group in groups:
        for hour in hours:
            if subjects[subject][hour - 1] != None:
                continue
            for s in subjects:
                if subjects[s][hour - 1] == group:
                    continue
                subjects[subject][hour - 1] = group
                break
            break

print(subjects)
