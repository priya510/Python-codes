import networkx as nx
import matplotlib.pyplot as plt
my_graph=nx.Graph()

my_graph.add_edges_from([
                    ("a","b"),
                    (2,3),
                    (3,4),
                    (4,5),
                    (2,4)])

nx.draw(my_graph,with_labels=True,font_weight='bold')
plt.show()
