"""
Profielwerkstuk - 6 VWO - roosteroptimalisatie
Door Sam Staijen en Joep van Dijk
"""
import argparse
from LPSolver import LPSolver
import utils
import time
import datatypes as types

if __name__ == "__main__":
    # TEMP VARIABLES
    # These variables store the data that will be used to get the result
    groups = [1, 2, 3, 4]
    teachers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    amount = [2, 2, 3, 2, 4, 2, 2, 3, 2]

    # Setup program variables
    lp = False

    # Parse args
    parser = argparse.ArgumentParser(description="Process arguments for this program")
    parser.add_argument("--lp", action='store_true', help="Select the linear programming solver")
    args = parser.parse_args()
    lp = args.lp

    solver = None

    timetable = types.Timetable([])

    # Select the right solver
    if lp == True:
        # Select the linear programming solver
        solver = LPSolver(timetable, 9, 5, groups, teachers, amount)
        utils.uprint("Solver found, using the linear programming solver")

    if solver == None:
        utils.uprint("Please specify a solver")
        exit()

    utils.uprint("Starting the solver")
    start_time = time.process_time()
    model = solver.solve()
    utils.uprint(model.num_nz)
    end_time = time.process_time()
    utils.uprint("Problem solved!")
    utils.uprint(f"Duration: {end_time - start_time}")