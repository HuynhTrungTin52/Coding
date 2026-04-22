# Monkeys, apes, gorillas are primates.
# Mice, squirrels, beavers are rodents.
# Crocodiles, Komodo dragons, lizards are reptiles.
# Coconut trees, grasses, oaks are plants.
# Mushrooms, molds, yeasts are fungi.
# And:
# Primates and rodents are mammals.
# Mammals, rodents, reptiles are animals.
# Animals, plants, mushrooms, molds are multicellular organisms.
# Yeasts are unicellular organisms.
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [
    ("Monkeys", "Primates"), ("Apes", "Primates"), ("Gorillas", "Primates"),
    ("Mice", "Rodents"), ("Squirrels", "Rodents"), ("Beavers", "Rodents"),
    ("Crocodiles", "Reptiles"), ("Komodo dragons", "Reptiles"), ("Lizards", "Reptiles"),
    ("Coconut trees", "Plants"), ("Grasses", "Plants"), ("Oaks", "Plants"),
    ("Mushrooms", "Fungi"), ("Molds", "Fungi"), ("Yeasts", "Fungi"),
    ("Primates", "Mammals"), ("Rodents", "Mammals"),
    ("Mammals", "Animals"), ("Rodents", "Animals"), ("Reptiles", "Animals"),
    ("Animals", "Multicellular organisms"), ("Plants", "Multicellular organisms"), 
    ("Mushrooms", "Multicellular organisms"), ("Molds", "Multicellular organisms"),
    ("Yeasts", "Unicellular organisms")
]

G.add_edges_from(edges)

plt.figure(figsize=(16, 12)) 

pos = nx.spring_layout(G, k=0.8, iterations=50)

nx.draw(
    G, 
    pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=3500,
    font_size=10,
    font_weight='bold',
    edge_color='gray',
    arrows=True,
    arrowstyle='-|>',  
    arrowsize=20
)

plt.show()