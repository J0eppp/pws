import PySimpleGUI as sg
from os.path import exists
from copy import deepcopy

from solver import LPSolver

from .parser import parse_json_file
from .datatypes import Timetable
from .GCSolver import GCSolver
from .LPSolver import LPSolver


class GUI:
    def __init__(self, args: dict):
        self.args = args
        sg.theme("DarkAmber")
        config_column = [
            [sg.Text("Please select a file"), sg.InputText(
                size=(50, 1), key="-FILENAME-"), sg.FileBrowse()],
            [sg.Button("Preload file", key="-PRELOADFILE-")],
            [sg.Checkbox("Linear programming solver", key="-LPSOLVER-"),
             sg.Checkbox("Graph colouring solver", key="-GCSOLVER-")],
            [sg.Button("Run")]
        ]
        info_column = [
            [sg.Text(size=(40, 1), key="-AMOUNTOFDAYSAWEEK-")],
            [sg.Text(size=(40, 1), key="-AMOUNTOFHOURSADAY-")],
            [sg.Text(size=(40, 1), key="-AMOUNTOFGROUPS-")],
            [sg.Text(size=(40, 1), key="-AMOUNTOFTEACHERS-")],
            [sg.Text(size=(40, 1), key="-AMOUNTOFSUBJECTS-")]
        ]
        start_column = [
            [sg.Column(config_column)]
        ]
        solver_column = [
            [sg.Text("Drawing")]
        ]
        self.layout = [
            [sg.Column(start_column, key="-START_COLUMN-")],
            [sg.Column(solver_column, key="-SOLVER_COLUMN-", visible=False)]
        ]
        self.window = sg.Window(
            "PWS roosteralgoritmes - Joep van Dijk & Sam Staijen", self.layout, margins=(200, 100), resizable=True).Finalize()

        self.timetable: Timetable = None
        self.solvers = []
        self.threads = []

    def draw_gc_solver(self, solver: GCSolver):
        return sg.Text("GC Solver")

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

            def parse_file():
                # Parse the file
                file_path = values["-FILENAME-"]
                # Check if a filename was given
                if len(file_path) == 0:
                    # Nope, no file was given
                    sg.popup_error("Please enter a file")
                # Check if it is a valid file
                elif exists(file_path) == False:
                    # Nope, the file does not exist
                    sg.popup_error("Please enter an existing file")
                # Check if it's a JSON file
                elif file_path.endswith(".json") == False:
                    # Nope, the extension is not JSON
                    sg.popup_error("Please enter a JSON file")
                else:
                    # Everything is fine
                    # Parse the file
                    self.timetable = parse_json_file(file_path)
                    print(self.timetable)
                    # Display data on the screen
                    self.window["-AMOUNTOFDAYSAWEEK-"].update(
                        f"Amount of days a week: {self.timetable.amount_of_days_a_week}")
                    self.window["-AMOUNTOFHOURSADAY-"].update(
                        f"Amount of hours a day: {self.timetable.amount_of_hours_a_day}")
                    self.window["-AMOUNTOFGROUPS-"].update(
                        f"Amount of groups: {len(self.timetable.groups)}")
                    self.window["-AMOUNTOFTEACHERS-"].update(
                        f"Amount of teachers: {len(self.timetable.teachers)}")
                    self.window["-AMOUNTOFSUBJECTS-"].update(
                        f"Amount of subjects: {len(self.timetable.subject_information)}")

            if event == "Run" or "-PRELOADFILE-":
                parse_file()

            if event == "Run":
                # Run the algorithm
                if self.timetable == None:
                    # The file was not preloaded, parse it now
                    parse_file()

                if values["-GCSOLVER-"] == True:
                    timetable: Timetable = deepcopy(self.timetable)
                    solver = GCSolver(timetable)
                    self.solvers.append(solver)
                if values["-LPSOLVER-"] == True:
                    timetable: Timetable = deepcopy(self.timetable)
                    solver = LPSolver(timetable)
                    self.solvers.append(solver)

                # self.window["-CONFIG_COLUMN-"].update(visible=False)
                # self.window["-INFO_COLUMN-"].update(visible=False)
                self.window["-START_COLUMN-"].update(visible=False)
                self.window["-SOLVER_COLUMN-"].update(visible=True)

                if len(self.solvers) == 1:
                    # We only have to draw one thing
                    # if values["-GCSOLVER-"] == True:
                    pass

        self.window.close()
