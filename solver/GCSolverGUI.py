from .SolverGUI import SolverGUI
from .GCSolver import GCSolver

# import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import networkx as nx


class GCSolverGUI(SolverGUI):
    """The GUI class for the graph colouring solver"""

    def __init__(self, solver: GCSolver):
        super().__init__("graph colouring", solver)

        self.fig = matplotlib.figure.Figure()

        self.ax = self.fig.add_subplot(111)

        self.fig_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas)

        # Run the solver
        self.solver.solve()

        # Draw things to the network
        network = self.solver.network
        node_colours = self.solver.node_colours
        pos = nx.spring_layout(network, k=0.75)
        nx.draw_networkx(network, pos, with_labels=True,
                         node_color=node_colours, ax=self.ax)
        self.fig_agg.draw()

        # TODO create a new thread that starts the algorithm to schedule hours and optimize the timetable

    def draw_figure(self, canvas):
        """Method to add figure to the canvas"""
        figure_canvas_agg = FigureCanvasTkAgg(self.fig, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
