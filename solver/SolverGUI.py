import PySimpleGUI as sg


from .Solver import Solver


class SolverGUI:
    """Base class for the solver GUI's"""

    def __init__(self, alg_type: str, solver: Solver):
        self.alg_type: str = alg_type
        self.solver: Solver = solver
        sg.theme("DarkAmber")
        layout = [
            [sg.Canvas(key="-CANVAS-")]
        ]
        self.window = sg.Window(
            f"PWS roosteralgoritmes - {self.alg_type}", layout, size=(200, 100), resizable=True, finalize=True)
