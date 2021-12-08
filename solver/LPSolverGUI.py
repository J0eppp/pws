from .SolverGUI import SolverGUI
from .LPSolver import LPSolver

import PySimpleGUI as sg


class LPSolverGUI(SolverGUI):
    """The GUI class for the linear programming solver"""

    def __init__(self, solver: LPSolver):
        super().__init__("linear programming",
                         solver, gui_layout=[
                             #  [sg.Text(size=(40, 10))]
                             [sg.Text(size=(50, 20), key="-LOG-")]
                         ])
        self.log_text = ""
        self.solver.log = self.log

        self.log("LOGGGG")

        self.solver.solve()

    def log(self, msg: str):
        print("Log")
        print(f"Msg: {msg}")
        self.log_text += msg + "\n"
        self.window["-LOG-"].update(self.log_text)
