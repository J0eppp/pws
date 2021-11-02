from .SolverGUI import SolverGUI
from .GCSolver import GCSolver

import matplotlib.pyplot as plt


class GCSolverGUI(SolverGUI):
    """The GUI class for the graph colouring solver"""

    def __init__(self, solver: GCSolver):
        super().__init__("graph colouring", solver)

        # TODO Do the graph things
