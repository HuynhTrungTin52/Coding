import matplotlib.pyplot as plt
import networkx as nx 
import numpy as np

A1 = np.array([
    [0, 0, 5, 3, 0, 0], #a
    [0, 0, 3, 2, 0, 0], #b
    [5, 3, 0, 1, 3, 0], #c
    [3, 2, 1, 0, 1, 3], #d
    [0, 0, 3, 1, 0, 4], #e
    [0, 0, 0, 3, 4, 0]  #f
])

A2 = np.array([
    [0, 0, 2, 3, 3, 0], #a
    [0, 0, 3, 2, 0, 0], #b
    [2, 3, 0, 2, 8, 6], #c
    [3, 2, 2, 0, 0, 5], #d
    [3, 0, 8, 0, 0, 3], #e
    [0, 0, 6, 5, 3, 0]  #f
])

G1=nx.from_numpy_array(A1)
pos=nx.spring_layout(G1)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
nx.draw_networkx(G1, pos=pos, with_labels=True, labels={a:b for a,b in enumerate('abcde')})
nx.draw_networkx_edge_labels(G1, pos=pos, font_size=6, label_pos=0.5)
plt.axis('equal')
plt.title('Graph 1')

plt.subplot(1, 2, 2)
G2 = nx.from_numpy_array(A2)
pos2 = nx.spring_layout(G2)
nx.draw_networkx(G2, pos=pos2, with_labels=True, labels={a:b for a,b in enumerate('abcdef')})
nx.draw_networkx_edge_labels(G2, pos=pos2, font_size=6, label_pos=0.5)
plt.axis('equal')
plt.title('Graph 2')
plt.axis('equal')
plt.show()