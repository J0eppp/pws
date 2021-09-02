#!/usr/bin/python3
# import csv
# import json

# input_file = "../data/Leerlingen met Vakkenpakket.csv"
# output_file = "../data/leerlingen_met_vakkenpakket.json"

# data = {}

# if __name__ == '__main__':
# 	with open(input_file) as file:
# 		reader = csv.DictReader(file)
# 		for rows in reader:
# 			for row in rows:
# 				print(row)


import csv
import json
import sys

for row in csv.DictReader(sys.stdin):
    json.dump(row, sys.stdout)
    sys.stdout.write('\n')
