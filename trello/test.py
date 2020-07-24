import trello_utils as t_utils
import networkx as nx
import nx_utils
import json

from operator import itemgetter

list_id = '5e64f121096f0e0d20806393'

fields = ['id', 'shortLink', 'desc', 'name', 'labels']

notes = t_utils.notes(list_id, fields)

print(f'First note is: \n{notes[0]}\n')

# Create the graph
G = nx_utils.graph_notes(notes)

print(f'len(G.nodes) = {len(G.nodes)}')
print(f'len(G.edges) = {len(G.edges)}\n')

print(f'G.nodes is: \n{G.nodes}\n')

# --- Obtain partition and modularity:

partition, modularity = nx_utils.partition_graph(G)

print('\nPartition using community(python-louvain):\n')

print(f'partition = \n{partition}\n')
print(f'modularity = {modularity}')

for n in G.nodes:
    G.nodes[n]['partition'] = partition[n]

# ----------------------------------------
# Export graph to graphML
# ----------------------------------------
nx.write_graphml(G, 'myslipbox.graphml')
print('\n--Exported graph to myslipbox.graphml')

G_data = nx_utils.graph_to_json(G)

# ----------------------------------------
# Export graph to JSON
# ----------------------------------------
print(f'\nExample of JSON data:')

print(f'First node:\n{G_data["nodes"][0]}')

print(f'First edge:{G_data["links"][0]}')


with open('myslipbox.json', 'w') as outfile:
    json.dump(G_data, outfile)

print('\n--Exported graph to myslipbox.json')
# -----------
