from create_graphos import Diagraphs
import networkx as nx3
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

g = Diagraphs()
g.create_graphs()
g.show_graphs_png()
g.show_graph()




