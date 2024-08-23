import networkx as nx
import random

a = [i for i in range(100)]
b = [(random.choices(a, k=2), random.random()) for i in range(random.randint(200, 400))]
b = list(map(lambda x: (x[0][0], x[0][1], x[1]), b))
g = nx.Graph()
g.add_weighted_edges_from(b)
nx.write_graphml_lxml(g, "graph.graphml")  