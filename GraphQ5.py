import networkx as nx
import matplotlib.pyplot as plt


G1 = nx.DiGraph()

G1.add_node(4)
G1.add_node(3)
G1.add_node(2)
G1.add_node(1)
G1.add_node(0)
G1.nodes()

G1.add_edge(0, 1, weight = 5)
G1.add_edge(1, 2, weight = 1)
G1.add_edge(1, 3, weight = 6)
G1.add_edge(2, 3, weight = 2)
G1.add_edge(4, 3, weight = 4)
G1.add_edge(4, 2, weight = 10)
G1.add_edge(4, 1, weight = 6)
G1.add_edge(0, 4, weight = 2)
G1.add_edge(0, 2, weight = 3)
G1.add_edge(2, 1, weight = 2)
G1.edges()

node_colors = ["blue" if n in nx.single_source_dijkstra_path_length(G1, source=4) else "red" for n in G1.nodes()]
pos = nx.spring_layout(G1)
weights = nx.get_edge_attributes(G1, "weight")
nx.draw_networkx(G1, pos, node_color=node_colors, with_labels=True)
nx.draw_networkx_edges(G1, pos, edge_color=node_colors)
nx.draw_networkx_edge_labels(G1, pos,  edge_labels=weights)


plt.title("Basic Graphs")
plt.gcf().canvas.set_window_title("")
plt.show()

# print Shortest path length from 4 to all reachable nodes
print("Shortest path length from 4 to all reachable nodes ")
print(nx.single_source_dijkstra_path_length(G1, source=4))

#Removing node 3
G1.remove_node(3)

# print Shortest path length from 4 to all reachable nodes after deleting 3
print("Shortest path length from 4 to all reachable nodes after Deleting 3")
print(nx.single_source_dijkstra_path_length(G1, source=4))

#Specifying node and edges color on the basis of shortest path length
node_colors = ["blue" if n in nx.single_source_dijkstra_path_length(G1, source=4) else "red" for n in G1.nodes()]
pos = nx.spring_layout(G1)
weights = nx.get_edge_attributes(G1, "weight")
nx.draw_networkx(G1, pos, node_color=node_colors, with_labels=True)
nx.draw_networkx_edges(G1, pos, edge_color=node_colors)
nx.draw_networkx_edge_labels(G1, pos, edge_labels=weights)

plt.title("Basic Graphs")
plt.gcf().canvas.set_window_title("")
plt.show()




