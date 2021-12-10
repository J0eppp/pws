klassen = [1, 2, 3]
vakken = [ (1, 2), (2, 4), (3, 2) ]
lessen = []

for klas in klassen:
	for vak in vakken:
		amount = vak[1]
		vak_id = vak[0]
		for _ in range(amount):
			lessen.append((klas, vak_id))
print(lessen)
print(f"Aantal lessen: {len(lessen)}")
print(f"Som aantal uren: {sum([x[1] for x in vakken])}")
