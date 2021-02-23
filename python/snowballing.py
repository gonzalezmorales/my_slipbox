from operator import itemgetter
import networkx as nx

# The following is based on Zinoviev, Dmitry. Complex Network Analysis in Python . Pragmatic Bookshelf. Kindle Edition.

SEED = 'NwHayaCP'

todo_lst = [(0, SEED)]  # The SEED is in the layer 0
todo_set = set(SEED)    # The SEED itself
done_set = set()        # Nothing is done yet

F = nx.DiGraph()
layer, page = todo_lst[0]

while layer < 3:
    del todo_lst[0]  # (1)
    done_set.add(page)
    print(layer, page)  # Show progress

    try:  # (2)
        wiki = wikipedia.page(page)
    except:
        layer, page = todo_lst[0]
        print("Could not load", page)
        continue

    for link in wiki.links:  # (3)
        link = link.title()
        if link not in STOPS and not link.startswith("List Of"):
            if link not in todo_set and link not in done_set:
                todo_lst.append((layer + 1, link))
                todo_set.add(link)
            F.add_edge(page, link)

    layer, page = todo_lst[0]  # (4)

print("{} nodes, {} edges".format(len(F), nx.number_of_edges(F)))

F.remove_edges_from(F.selfloop_edges())
duplicates = [(node, node + "s") for node in F if node + "s" in F]
for dup in duplicates:
    F = nx.contracted_nodes(F, *dup, self_loops=False)
duplicates = [(x, y) for x, y
              in [(node, node.replace("-", " ")) for node in F]
              if x != y and y in F]
for dup in duplicates:
    F = nx.contracted_nodes(F, *dup, self_loops=False)
nx.set_node_attributes(F, 0, "contraction")

core = [node for node, deg in dict(F.degree()).items() if deg >= 2]
G = nx.subgraph(F, core)
print("{} nodes, {} edges".format(len(G), nx.number_of_edges(G)))
# 2995 nodes, 11817 edges
nx.write_graphml(G, "cna.graphml")

top_indegree = sorted(dict(G.in_degree()).items(),
                      reverse=True, key=itemgetter(1))[:100]
print("\n".join(map(lambda t: "{} {}".format(*reversed(t)), top_indegree)))
