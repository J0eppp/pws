"""
Profielwerkstuk - 6 VWO - roosteroptimalisatie
Door Sam Staijen en Joep van Dijk
"""
import argparse
from LPSolver import LPSolver
import utils
import time
import datatypes as types
import json

if __name__ == "__main__":
    # TEMP VARIABLES
    # These variables store the data that will be used to get the result
    # groups = [1, 2, 3]
    # teachers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # amount = [2, 2, 3, 2, 4, 2, 2, 3, 2]

    # Setup program variables
    lp = False

    # Parse args
    parser = argparse.ArgumentParser(description="Process arguments for this program")
    parser.add_argument("--lp", action='store_true', help="Select the linear programming solver")
    parser.add_argument("-d", "--data", type=str, help="Select the JSON file")
    args = parser.parse_args()
    lp = args.lp
    data_file = args.data

    if data_file == None:
        utils.uprint("Please specify an input file with the -d/--data argument")
        exit()
    
    utils.uprint("-==================================-")
    utils.uprint("Reading and parsing the file....")
    start_time = time.process_time()
    file = open(data_file, "r")
    data = json.load(file)
    file.close()
    end_time = time.process_time()
    utils.uprint("Done reading and parsing the file")
    utils.uprint(f"Reading and parsing the file took {end_time - start_time} seconds")
    utils.uprint("-==================================-")

    amount_of_days_per_week = data["amountOfDaysPerWeek"]
    amount_of_hours_per_day = data["amountOfHoursPerDay"]
    groups = data["groups"]
    teachers = data["teachers"]
    amount = data["amount"]
    


    solver = None

    timetable = types.Timetable([])

    # Select the right solver
    if lp == True:
        # Select the linear programming solver
        solver = LPSolver(timetable, amount_of_hours_per_day, amount_of_days_per_week, groups, teachers, amount)
        utils.uprint("-==================================-")
        utils.uprint("Solver found, using the linear programming solver")

    if solver == None:
        utils.uprint("Please specify a solver")
        exit()
    

    utils.uprint("Starting the solver")
    utils.uprint("-==================================-")
    start_time = time.process_time()
    model = solver.solve()
    utils.uprint(model.num_nz)
    end_time = time.process_time()
    utils.uprint("Problem solved!")
    utils.uprint(f"Duration: {end_time - start_time}")