import PySimpleGUI as sg


from .Solver import Solver


class SolverGUI:
    """Base class for the solver GUI's"""

    def __init__(self, alg_type: str, solver: Solver, gui_layout=None):
        self.alg_type: str = alg_type
        self.solver: Solver = solver
        sg.theme("DarkAmber")
        layout = gui_layout
        if layout == None:
            layout = [
                [sg.Canvas(key="-CANVAS-")]
            ]
        self.window = sg.Window(
            f"PWS roosteralgoritmes - {self.alg_type}", layout, size=(1080, 720), resizable=True, finalize=True)
