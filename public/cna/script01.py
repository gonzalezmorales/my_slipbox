import networkx as nx


'''
    NetwrokX supports 4 graph types:
    1. Undirected graphs
    2. Directed graphs
    3. Multigraphs
    4. Directed multigraphs
'''

# Create an empty undirected graph:

G1 = nx.Graph()

# Create an empty directed graph (digraph):

G2 = nx.DiGraph()

# Convert a digraph into an undirected graph:

G2b = nx.Graph(G2)

# Create an empty multigraph:

G3 = nx.MultiGraph()

# Create an empty directed multigraph:

G4 = nx.MultiDiGraph()

# ======================================
# Add and remove nodes and edges
# ======================================

'''
    NetworkX provides several mechanisms for adding
    nodes and edges to an existing graph:
    - One by one
    - From a list
    - From another graph

    Likewise, you can remove nodes or edges
    - One by one
    - From a list

    Rules for node and edge manipulations:
    - Adding and edge ensures that its end are also
      added if they did not exist before
    - Adding a duplicate node or edge is silently
      ignored unless except in case of a multigraph
      (in which case an additional parallel edge is
      created).
    - Removing an edge does not remove its end nodes
    - Removing a single non-existent node or edge
      rises a 'Network Error' exception, but if the
      node or edge is part of a list, then an error
      is silently ignored
'''
G = nx.Graph([('A', 'eggs'), ])
# Add a single node:
G.add_node('spniach')

# add a single node by mistake:
G.add_node('Hg')

# add a list of nodes:
G.add_nodes_from(['folates', 'asparagus', 'liver'])

# add one edge when both ends exist:
G.add_edge('spinach', 'folates')

# add one edge by mistake:
G.add_edge('spniach', 'heating oil')

# add one edge, one end does not exit:
G.add_edge('liver', 'Se')

# add edges from a list:
G.add_edges_from([('folates', 'liver'), ('folates', 'asparagus')])

# remove unwanted node:
G.remove_node('Hg')

# It is safe to remove a missing node using a list:
G.remove_nodes_from(['Hg', ])

# Remove unwanted edge:
G.remove_edge('spniach', 'heating oil')

# It is safe to remove a missing edge using a list:
G.remove_edges_from([('spinach', 'heating oil'), ])

# Remove unwanted node (not removed yet):
G.remove_node('heating oil')


# ======================================
# Look at Edge and Node Lists
# ======================================

'''
    The attributes .nodes and .edges from the Graph object
    store all nodes and edges, respectively, in the form of
    'NodeView' and 'EdgeView'
'''

# The repr() function returns a printable representation of the given object

print(repr(G.nodes))
print(G.nodes)

print('---')

print(repr(G.edges))
print(G.edges)

'''
    Calling the methods nodes() and edges() on the Graph object
    without any parameters returns the same views as their
    attribute counterparts:
'''
print('---')
print(G.nodes())
print(G.edges())

'''
    Calling the methods nodes() and edges() on the Graph object
    with the optional parameter 'data=True' returns the views
    'NodeDataView' and 'EdgeDataView' with the additional attributes
    as dictionaries
'''
print('---')
print(repr(G.nodes(data=True)))
print(G.nodes(data=True))
print('---')
print(repr(G.edges(data=True)))
print(G.edges(data=True))

'''
    You can measure the length of the returned views to find out
    the number of nodes and edges.

    Additionally, the function 'len(G)' returns the number of
    nodes in G.
'''

print(f'len(G)={len(G)}')
print(f'len(G.nodes)={len(G.nodes)}')
print(f'len(G.edges)={len(G.edges)}')


# ======================================
# Add attributes
# ======================================

'''
    A node or edge attribute describe its non-structural
    properties.  'NetworkX' provides mechanisms for 
    setting, changing, and comparing attributes.

    An attribute is implemented as a dictionary associated 
    with the node or edge.

'''
