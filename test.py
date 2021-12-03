for i in range(3):
	print(f"i: {i}")
	for j in range(4):
		print(f"j: {j}")
		if j == 2:
			print("Break!")
			break
		for k in range(3):
			print(f"k: {k}")
