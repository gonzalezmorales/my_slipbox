import trello_utils as t_utils
import myslipbox_utils as sb_utils
import networkx as nx


list_id = '5e64f121096f0e0d20806393'
fields = ['id', 'shortLink', 'desc', 'name', 'labels']

notes = t_utils.read_cards(list_id, fields)

clean_notes = []

# Clean notes
for n in notes:
    clean_notes.append(sb_utils.split_content(n))

# Example:
print('--- Example of a clean note:')
print(clean_notes[0])
print('---\n')

# ---------------------------------------------------
# Create graph using networkx
# ----------------------------------------------------

# Create an empty undirected graph:

G = nx.Graph()

# add edges from a list:

for n in clean_notes:
    node_from = n['shortLink']

    attributes = {}

    attributes['id'] = n['shortLink']
    attributes['name'] = n['name']
    attributes['labels'] = n['labels']
    attributes['text_md'] = n['text_md']
    attributes['quotes'] = n['quotes']
    attributes['sources'] = n['sources']

    G.add_nodes_from([(node_from, attributes), ])

    for node_to in n['links']:
        G.add_edges_from([(node_from, node_to)])


print(G.nodes)
print(G.edges)

print('---')
print(f'len(G.nodes)={len(G.nodes)}')
print(f'len(G.edges)={len(G.edges)}')

# ----------------------------------
# AtlasView: Shows all the edges of a node and their
# attributes

print('---')
print(repr(G['Lr60zbkO']))

# -----------------------------------
# Add attributes
# -----------------------------------

print(G.nodes['Lr60zbkO'])
