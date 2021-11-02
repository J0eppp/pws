import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from os.path import exists
from copy import deepcopy
import threading

from solver import LPSolver
from solver.GCSolverGUI import GCSolverGUI

from .parser import parse_json_file
from .datatypes import Timetable
from .GCSolver import GCSolver
from .LPSolver import LPSolver


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


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
            [sg.Column(config_column), sg.VSeperator(), sg.Column(info_column)]
        ]
        self.layout = start_column
        self.window = sg.Window(
            "PWS roosteralgoritmes - Joep van Dijk & Sam Staijen", self.layout, margins=(200, 100), resizable=True).Finalize()

        self.timetable: Timetable = None
        self.solvers = []
        self.guis = []

    def run(self):
        while True:
            # event, values = self.window.read()
            window, event, values = sg.read_all_windows()

            def parse_file():
                # Parse the file
                file_path = values["-FILENAME-"]
                # Check if a filename was given
                if file_path == None:
                    return
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

            if event == sg.WIN_CLOSED:
                if window == self.window:
                    # Close all other windows and kill all threads
                    for gui in self.guis:
                        gui.window.close()
                    break
                else:
                    for gui in self.guis:
                        if gui.window == window:
                            gui.window.close()
                            self.guis.remove(gui)

            elif event == "-PRELOADFILE-":
                parse_file()

            elif event == "Run":
                # Create the windows necessary
                if self.timetable == None:
                    # The file was not preloaded, parse it now
                    parse_file()

                if values["-GCSOLVER-"] == True:
                    # Start a new window with a GCSolver
                    timetable: Timetable = deepcopy(self.timetable)
                    solver = GCSolver(timetable)
                    self.solvers.append(solver)
                    gui = GCSolverGUI(solver)
                    self.guis.append(gui)
                if values["-LPSOLVER-"] == True:
                    timetable: Timetable = deepcopy(self.timetable)
                    solver = LPSolver(timetable)
                    self.solvers.append(solver)
                    # Start a new window with a LPSolver

        self.window.close()
