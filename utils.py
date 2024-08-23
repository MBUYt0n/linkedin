import json
from node import Node
import networkx as nx
import matplotlib.pyplot as plt


def read_graph():
    with open("data.json", "r") as f:
        data = json.load(f)

    graph = [Node(i["user"]) for i in data]
    for i in range(len(data)):
        for j in data[i]["edges"]:
            graph[i].read_edge(j[0], j[1])

    return graph

def plot_graph(graph):
    G = nx.Graph()
    for node in graph:
        G.add_node(node.user)
        for edge in node.edges:
            G.add_edge(node.user, edge[0], weight=edge[1])

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.savefig('graph.png')
