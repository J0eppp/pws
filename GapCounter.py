def countGapHours() -> int:timetable = [[[]]]

for (d, h, g, _) in S:
    timetable[g][d].append(h)
    gap_hours = 0
    for g in timetable:
        for d in timetable[g]:
            arr = timetable[g][d]
            arr = arr.sort()
            first = arr[0]
            last = arr[-1]
            amount = last - (first - 1) - len(arr)
            gap_hours += amount
            return gap_hours