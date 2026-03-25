from create_graphos import Dgraphs
import networkx as nx3
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

g = Dgraphs()
g.create_graphs()
g.show_graphs_png()
g.show_graph()




