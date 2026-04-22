import numpy as np
import networkx as nx
M = np.array([
    [0, 0, 2, 3, 3, 0], #a
    [0, 0, 3, 2, 0, 0], #b
    [2, 3, 0, 2, 8, 6], #c
    [3, 2, 2, 0, 0, 5], #d
    [3, 0, 8, 0, 0, 3], #e
    [0, 0, 6, 5, 3, 0]  #f
])
G = nx.from_numpy_array(M)
edge_list = list(G.edges(data='weight'))
print(edge_list)