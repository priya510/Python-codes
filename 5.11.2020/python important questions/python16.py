import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])
G.add_edge(1,2)
edge=("d","e")
G.add_edge(*edge)
edge=("a","b")
G.add_edge(*edge)
G.add_edges_from([("a","c"),("c","d"),("a",1),(1,"d"),("a",2)])
nx.draw(G)
plt.show()
