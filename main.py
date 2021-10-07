from argparse import ArgumentParser
# from . import utils
import solver.utils as utils
from solver.parser import parse_json_file
import time
from solver.datatypes import Timetable
from solver.LPSolver import LPSolver

SEPERATION_STRING = "-==================================-"


def main():
    parser = ArgumentParser(description="Process arguments for this program")
    parser.add_argument("-s", "--solver", type=str,
                        help="Select the linear programming solver")
    parser.add_argument("-d", "--data", type=str, help="Select the JSON file")
    args = parser.parse_args()
    data_file = args.data

    # Parse the CLI arguments
    if data_file == None:
        utils.uprint(
            "Please specify an input file with the -d/--data argument")
        return

    if args.solver == None:
        utils.uprint("Please specify a solving method")
        utils.uprint("Available solving methods:")
        utils.uprint("    1. Linear programming (lp)")
        return

    # Read and parse the file with all the data
    utils.uprint(SEPERATION_STRING)
    utils.uprint("Reading and parsing the file....")
    start_time = time.process_time()
    timetable: Timetable = parse_json_file(data_file)
    end_time = time.process_time()
    utils.uprint("Done reading and parsing the file")
    utils.uprint(
        f"Reading and parsing the file took {end_time - start_time} seconds")
    utils.uprint("Loaded {amount_of_groups} group{multiple_groups} and {amount_of_teachers} teacher{multiple_teachers}".format(amount_of_groups=len(
        timetable.groups), amount_of_teachers=len(timetable.teachers), multiple_groups="s" if len(timetable.groups) > 1 else "", multiple_teachers="s" if len(timetable.teachers) > 1 else ""))
    utils.uprint(SEPERATION_STRING)

    solver = None

    # Select solver
    if args.solver == "lp":
        solver = LPSolver(timetable)

    timetable = solver.solve()


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    utils.uprint(SEPERATION_STRING)
    utils.uprint(f"Total execution time is {end_time - start_time} seconds")
    utils.uprint(SEPERATION_STRING)
