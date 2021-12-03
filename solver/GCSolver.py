import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from itertools import combinations
from random import shuffle
from time import time
from math import floor

from .Solver import Solver
from .datatypes import Timetable, Lesson
from .utils import uprint
from .Prettyprint import pretty_print


SEPERATION_STRING = "-==================================-"


class GCSolver(Solver):
    def __init__(self, timetable: Timetable, display=False, save=None):
        self.timetable = timetable
        self.network = nx.Graph()
        self.display = display
        self.save = save
        self.fig = plt

        self.node_colours = None

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        uprint(SEPERATION_STRING)
        uprint("Sorting data")
        start_time = time()

        subjects = []
        for si in self.timetable.subject_information:
            try:
                subjects.index(si.subject)
            except ValueError:
                subjects.append(si.subject)

        # Create a dictionary for the subject information
        subject_information = {}
        for subject in subjects:
            subject_information[f"{subject}"] = {}
        for si in self.timetable.subject_information:
            # subject_information[si.subject][si.year] = si
            # subject_information.update({f"{si.subject}": {f"{si.year}": si}})
            # subject_information[f"{si.subject}"] = { f"{si.year}": si }
            # subject_information[f"{si.subject}"] = subject_information[f"{si.subject}"].update({ f"{si.year}": si })
            subject_information[f"{si.subject}"][f"{si.year}"] = si

        # Create a dictionary for the teachers based on subject
        teachers = {}
        for teacher in self.timetable.teachers:
            teachers.update({f"{teacher.subject}": teacher})

        end_time = time()

        uprint("Done sorting data")
        uprint(f"Sorting data took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        lessons = []
        labels = {}

        uprint(SEPERATION_STRING)
        uprint("Creating all necessary lesson objects")
        start_time = time()

        # Create all necessary lessons
        for group in self.timetable.groups:
            for subject in group.subjects:
                si = subject_information[subject][f"{group.year}"]
                teacher = sorted([teacher for teacher in self.timetable.teachers if teacher.subject == si.subject], key=lambda x: x.selected_amount)[0]
                teacher.selected_amount += 1
                for _ in range(si.amount):
                    lessons.append(
                        Lesson(len(lessons), teacher, group, None, None, si, 0))
                    labels.update({len(lessons) - 1: si.subject})

        end_time = time()
        uprint(f"Done creating {len(lessons)} lesson objects")
        uprint(f"Creating lesson objects took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        # Add all the nodes to the network
        uprint(SEPERATION_STRING)
        uprint("Adding nodes to the network")
        start_time = time()

        self.network.add_nodes_from(
            [lesson.identifier for lesson in lessons])

        end_time = time()
        uprint(
            f"Adding nodes to the network took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        # Create connections
        uprint(SEPERATION_STRING)
        uprint("Creating connections in the network")
        start_time = time()

        for (l1, l2) in combinations(lessons, 2):
            if l1.group == l2.group or l1.teacher == l2.teacher:
                self.network.add_edge(l1.identifier, l2.identifier, weight=1)

        end_time = time()
        uprint("Done creating connections")
        uprint(f"Creating connections took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        # colours = list(
        #     set(list(mcolors.CSS4_COLORS.keys())) | set(list(mcolors.BASE_COLORS.keys())))
        colours = list(mcolors.CSS4_COLORS.keys())
        colours = colours[0:max(dict(self.network.degree).values())][0:45]

        hours = range(45)
        calendar = {}
        for hour in hours:
            calendar[hour] = []

        # Map each color to an hour
        from_color_to_hour = {col: hours[i] for i, col, in enumerate(colours)}

        uprint(SEPERATION_STRING)
        uprint("Running the greedy algorithm to give the nodes a colour")
        start_time = time()

        # Greedy algorithm
        nodes = list(self.network.nodes())
        shuffle(nodes)  # Randomly shuffle the nodes
        for node in nodes:
            dict_neighbors = dict(self.network[node])
            nodes_neighbors = list(dict_neighbors.keys())

            forbidden_colours = []
            for neighbor in nodes_neighbors:
                if len(self.network.nodes.data()[neighbor].keys()) == 0:
                    continue
                else:
                    # If this neighbor has a colour, this colour is forbidden to use for this colour
                    forbidden_colours.append(
                        self.network.nodes.data()[neighbor]["color"])

            # Assign a colour that is not forbidden
            for colour in colours:
                if colour in forbidden_colours:
                    continue
                else:
                    self.network.nodes[node]["color"] = colour
                    break

        node_colours = [data["color"]
                        for _, data in self.network.nodes(data=True)]

        end_time = time()
        uprint("The greedy algorithm is done")
        uprint(f"The greedy algorithm took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        uprint(SEPERATION_STRING)
        uprint("Graph info: ")

        # Get all the unique colours
        uprint(f"The graph needs {len(list(set(node_colours)))} colours")

        uprint(f"The graph has {len(self.network.edges)} edges")
        uprint(SEPERATION_STRING)

        for v, data in self.network.nodes(data=True):
            calendar[from_color_to_hour[data['color']]].append(v)

        # pretty_print(self.timetable)

        # Draw everything
        self.node_colours = [data["color"]
                             for v, data in self.network.nodes(data=True)]
        # self.node_colours = node_colours

        if self.display == True:
            # Display
            pos = nx.spiral_layout(self.network)
            nx.draw_networkx(self.network, pos, with_labels=True,
                             node_color=self.node_colours, node_size=60, font_size=8)
            plt.show()

        if self.save != None:
            uprint(SEPERATION_STRING)
            uprint(f"Saving the graph to: {self.save}")
            pos = nx.spiral_layout(self.network)
            nx.draw_networkx(self.network, pos, with_labels=True,
                             node_color=self.node_colours, node_size=60, font_size=8)
            self.fig.axis('off')
            self.fig.gca().set_position([0, 0, 1, 1])
            start_time = time()
            # plt.savefig(self.save, format="svg", dpi=600)
            # self.fig.savefig(self.save, format=str(self.save).split(".")[-1], dpi=600)
            self.fig.savefig(self.save)
            end_time = time()
            uprint("Done saving the graph")
            uprint(
                f"Saving the graph took {end_time - start_time} seconds")

        return self.timetable
