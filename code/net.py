import networkx as nx
from common_functions import get_data

import matplotlib.pyplot as plt

G = nx.Graph()

node_header, node_data = get_data("filtered_nodes.tsv")

edge_header, edge_data = get_data("edges.tsv")

for node in node_data:
    print(node)
    G.add_node(int(node[0]), name=node[1], chinese_name=node[2], index_year=int(node[3]))

for edge in edge_data:
    print(edge)
    G.add_edge(int(edge[0]), int(edge[1]), kin=edge[2], label=edge[3])

degree_centrality = nx.degree_centrality(G)
between_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

for node in nx.nodes(G):
    print(node.name)

# # draw the network
# nx.draw_spring(G)
# plt.show()