import pandas as pd
import json
import collections, functools, operator

nodes_df = pd.read_json("src/data/nodes.json")
with open('src/data/nodes.json') as json_file:
    nodes = json.load(json_file)

edges_df = pd.read_json("src/data/edges.json")
with open('src/data/edges.json') as json_file:
    edges = json.load(json_file)


nodes_df.to_excel("output/nodes.xlsx")  
edges_df.to_excel("output/edges.xlsx")  

#------------------------------------
# Calculate the density of the graph
#------------------------------------


''' n = len(nodes)
print(f'n = {n}')

# Total number of edges:
e = 0
for i in nodes:
    e = e + len(i['links'])
print(f'e = {e}')


d = e / (n*(n-1)/2)
print(f'd = {d}') '''

def describe(nodes):
    # Total number of nodes:
    n = len(nodes)
    # Total number of edges:
    e = 0
    for i in nodes:
        e = e + len(i['links'])
    e = e / 2
    # Density:
    d = e / (n*(n-1)/2)
    return({'n_nodes': n, 'n_edges': e, 'density': d})

print(describe(nodes))


def egonet_density(nodes):
    egonet_density = []
    for i in nodes:
        egonet = []
        for j in nodes:
            if j['id'] not in i['links']:
                continue
            d = {
                    'id': j['id'],
                    'links': [k for k in j['links'] if k in i['links']]
                }

            egonet.append(d)

        if len(egonet)>1:
            egonet_density.append(
                {
                    'id': i['id'],
                    'egonet_density' : describe(egonet)['density']
                }
            )
        else:
            egonet_density.append(
                {
                    'id': i['id'],
                    'egonet_density' : None
                }
            )
    return egonet_density

print(egonet_density(nodes))


egonet_densities = egonet_density(nodes)

x = []
for i in nodes:
    r = dict()

    r['id'] = i['id']
    r['links'] = i['links']
    r['degree'] = len(i['links'])
    for j in egonet_densities:
        if j['id'] != i['id']:
            continue
        r['egonet_density'] = j['egonet_density']
    if r['egonet_density']:
        r['degree_x_egodens'] = r['degree'] * r['egonet_density'] 
    else:
        r['degree_x_egodens'] = 0
    x.append(r)
    
x = sorted(x, key = lambda i: i['degree_x_egodens'],reverse=True)



pd.DataFrame(x).to_excel("output/x.xlsx")  

list_of_processed = []

summaries = []

for i in x:
    
    if i['id'] in list_of_processed:
        continue

    s1=dict()
    s1['id'] = i['id']
    s1['s2'] = []

    list_of_processed.append(i['id'])

    for j in [x for x in i['links'] if x not in list_of_processed] :
        s2 = dict()
        for ii in x:
            if ii['id'] != j:
                continue
            s2['id'] = ii['id']
            s2['s3'] = []

            list_of_processed.append(ii['id'])
            
            for jj in [x for x in ii['links'] if x not in list_of_processed]:
                s3 = dict()
                for iii in x:
                    if iii['id'] != jj:
                        continue
                    s3['id'] = iii['id']
                    list_of_processed.append(iii['id'])
                s2['s3'].append(s3)
            s1['s2'].append(s2)
    summaries.append(s1)
            

with open('output/summaries.json', 'w') as outfile:
    json.dump(summaries, outfile, indent=4)

reporte = []
for s1 in summaries:
    if len(s1['s2'])==0:
        continue
    r = dict()
    r['level'] = 1
    r['id'] = s1['id']
    for i in nodes:
        if i['id'] != s1['id']:
            continue
        r['title'] = i['name']
        r['text'] = i['text_md']
    
    reporte.append(r)

    for s2 in s1['s2']:
        r = dict()
        r['level'] = 2
        r['id'] = s2['id']
        for i in nodes:
            if i['id'] != s2['id']:
                continue
            r['title'] = i['name']
            r['text'] = i['text_md']

        reporte.append(r)

        for s3 in s2['s3']:
            r = dict()
            r['level'] = 3
            r['id'] = s3['id']
            for i in nodes:
                if i['id'] != s3['id']:
                    continue
                r['title'] = i['name']
                r['text'] = i['text_md']


            reporte.append(r)



with open('output/reporte.json', 'w') as outfile:
    json.dump(reporte, outfile, indent=4)


pd.DataFrame(reporte).to_excel("output/reporte.xlsx")  
