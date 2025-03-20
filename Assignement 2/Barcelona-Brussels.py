#r: networkx
#r: matplotlib

import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

#create a Graph
G = nx.Graph()

#add nodes (cities)
G.add_node('Barcelona')
G.add_node('Paris')
G.add_node('Brussels')
G.add_node('Amsterdam')

#add edges (connections with travel times in hours)
G.add_edge('Barcelona', 'Paris', weight=6)
G.add_edge('Paris', 'Brussels', weight=1.5)
G.add_edge('Paris', 'Amsterdam', weight=3.5)
G.add_edge('Amsterdam', 'Brussels', weight=2)

#compute shortest path from Barcelona to Brussels
shortest_path = nx.shortest_path(G, source='Barcelona', target='Brussels', weight='weight')

#add position to display
pos = nx.spring_layout(G, seed=42)

#draw settings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('Fastest Route from Barcelona to Brussels', fontsize=12)

#draw nodes
nx.draw(G, pos, node_size=1500, with_labels=True, node_color='red', font_size=10, font_color='white')

#draw edges
nx.draw_networkx_edges(G, pos, width=1.5)

#highlight shortest path in blue
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='blue')

#display travel times on edges
edge_labels = {(u, v): f"{d['weight']}h" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

#save the graph
path = r"C:\Users\Sara Guessous\Desktop\session02\images\Fastest_Route_Barcelona_Brussels.png"
plt.savefig(path, format="PNG")

#show the graph
plt.tight_layout()
plt.show()

