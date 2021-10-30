import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from itertools import combinations
from random import shuffle
from time import process_time

from .Solver import Solver
from .datatypes import Timetable, Lesson
from .utils import uprint


SEPERATION_STRING = "-==================================-"


class GCSolver(Solver):
    def __init__(self, timetable: Timetable, display=False):
        self.timetable = timetable
        self.network = nx.Graph()
        self.display = display

    def solve(self) -> Timetable:
        return self.__solve()

    def __solve(self) -> Timetable:
        uprint(SEPERATION_STRING)
        uprint("Sorting data")
        start_time = process_time()

        # Create a dictionary for the subject information
        subject_information = {}
        for si in self.timetable.subject_information:
            # subject_information[si.subject][si.year] = si
            subject_information.update({f"{si.subject}": {f"{si.year}": si}})

        # Create a dictionary for the teachers based on subject
        teachers = {}
        for teacher in self.timetable.teachers:
            teachers.update({f"{teacher.subject}": teacher})

        end_time = process_time()

        uprint("Done sorting data")
        uprint(f"Sorting data took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        lessons = []
        labels = {}

        uprint(SEPERATION_STRING)
        uprint("Creating all necessary lesson objects")
        start_time = process_time()

        # Create all necessary lessons
        for group in self.timetable.groups:
            for subject in group.subjects:
                si = subject_information[subject][f"{group.year}"]
                for _ in range(si.amount):
                    lessons.append(
                        Lesson(len(lessons), teachers[si.subject], group, None, None, si, 0))
                    labels.update({len(lessons) - 1: si.subject})

        end_time = process_time()
        uprint("Done creating lesson objects")
        uprint(f"Creating lesson objects took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        # Add all the nodes to the network
        uprint(SEPERATION_STRING)
        uprint("Adding nodes to the network")
        start_time = process_time()

        self.network.add_nodes_from(
            [lesson.identifier for lesson in lessons])

        end_time = process_time()
        uprint(
            f"Adding nodes to the network took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        # Create connections
        uprint(SEPERATION_STRING)
        uprint("Creating connections in the network")
        start_time = process_time()

        for (l1, l2) in combinations(lessons, 2):
            if l1.group == l2.group or l1.teacher == l2.teacher:
                self.network.add_edge(l1.identifier, l2.identifier)

        end_time = process_time()
        uprint("Done creating connections")
        uprint(f"Creating connections took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        # colours = list(
        #     set(list(mcolors.CSS4_COLORS.keys())) | set(list(mcolors.BASE_COLORS.keys())))
        colours = list(mcolors.CSS4_COLORS.keys())
        colours = colours[0:max(dict(self.network.degree).values())]

        hours = range(45)
        calendar = {}
        for hour in hours:
            calendar[hour] = []

        # Map each color to an hour
        # from_color_to_hour = {col: hours[i] for i, col, in enumerate(colours)}

        uprint(SEPERATION_STRING)
        uprint("Running the greedy algorithm to give the nodes a colour")
        start_time = process_time()

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

        end_time = process_time()
        uprint("The greedy algorithm is done")
        uprint(f"The greedy algorithm took {end_time - start_time} seconds")
        uprint(SEPERATION_STRING)

        uprint(SEPERATION_STRING)
        uprint("Graph info: ")

        # Get all the unique colours
        uprint(f"The graph needs {len(list(set(node_colours)))} colours")

        uprint(f"The graph has {len(self.network.edges)} edges")
        uprint(SEPERATION_STRING)

        if self.display == True:
            # Draw it
            node_colours = [data["color"]
                            for v, data in self.network.nodes(data=True)]

            subax1 = plt.subplot()
            pos = nx.spring_layout(self.network, k=0.75)
            nx.draw_networkx(self.network, pos, with_labels=True,
                             node_color=node_colours)
            plt.show()
