import json
import requests
import re
import copy

url = "https://api.trello.com/1/lists/5e64f121096f0e0d20806393/cards?fields=id,shortLink,desc,name,labels"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
notes = response.json()


def split_content(card):
    '''Split desc into 
       - text_md (main text in markdown)
       - links (linked notes)
       - quotes (linked quotes), and
       - sources (list of sources)
    '''

    card_new = copy.deepcopy(card)

    content = card_new['desc'].split('---')

    text_md = content[0]

    iterx = iter(re.split('https://trello.com/c/', content[1]))
    next(iterx)
    links = []
    for i in iterx:
        links.append(i.replace(' ', '').replace('-', '').replace('\n', ''))

    iterx = iter(re.split('https://trello.com/c/', content[2]))
    next(iterx)
    quotes = []
    for i in iterx:
        quotes.append(i.replace(' ', '').replace('-', '').replace('\n', ''))

    iterx = iter(re.split('https://trello.com/c/', content[3]))
    next(iterx)
    sources = []
    for i in iterx:
        sources.append(i.replace(' ', '').replace('-', '').replace('\n', ''))

    card_new['text_md'] = text_md
    card_new['links'] = links
    card_new['quotes'] = quotes
    card_new['sources'] = sources
    card_new.pop('desc')

    return card_new


def generate_edges(graph):
    '''Generate edges based on graph file'''
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append({'source': node, 'target': neighbour})
    return edges


clean_notes = []

# Clean notes
for n in notes:
    clean_notes.append(split_content(n))


# Generate graph:
graph = dict()

for n in clean_notes:
    graph[n['shortLink']] = set(n['links'])

# Ensure all links are bi-directional in the graph:
for k, v in graph.items():
    for i in v:
        graph[i].add(k)

# clean notes
for n in clean_notes:
    n['links'] = list(graph[n['shortLink']])
    n['id'] = n['shortLink']
    n['n_links'] = len(n['links'])
    n.pop('shortLink')


with open('src/data/nodes.json', 'w') as outfile:
    json.dump(clean_notes, outfile)


with open('src/data/edges.json', 'w') as outfile:
    json.dump(generate_edges(graph), outfile)
