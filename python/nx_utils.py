
import networkx as nx
from community import community_louvain
from networkx.readwrite import json_graph


def graph_notes(notes):
    '''
       Create graph using networkx
    '''
    G = nx.Graph()

    for n in notes:

        node_from = n['shortLink']
        G.add_node(node_from)

        for node_to in n['links']:
            G.add_edge(node_from, node_to)

    for n in notes:
        G.nodes[n['shortLink']]['name'] = n['name']
        G.nodes[n['shortLink']]['text_md'] = n['text_md']
        G.nodes[n['shortLink']]['labels'] = ','.join(n['labels'])
        G.nodes[n['shortLink']]['quotes'] = ','.join(n['quotes'])
        G.nodes[n['shortLink']]['sources'] = ','.join(n['sources'])

    return G


def partition_graph(G):
    '''
       Calculate partition using community (python-louvain).
       High modularity means that the partition describes
       a very good community structure.
    '''
    partition = community_louvain.best_partition(G)
    modularity = community_louvain.modularity(partition, G)
    return partition, modularity


def graph_to_json(G):
    data = json_graph.node_link_data(G)
    return data
