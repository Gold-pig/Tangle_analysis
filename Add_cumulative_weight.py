import matplotlib.pyplot as plt
import networkx as nx
import json

with open("branch_link_2016.json") as f0:
    branch_link = json.load(f0)

with open("trunk_link_2016.json") as f1:
    trunk_link = json.load(f1)

with open("transactions_2016 with c_weight_correct.json") as f:
    data = json.load(f)

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

print(len(data))
for i in range(len(data)):
    G.add_node(i, weight=data[i]['cumulative weight'])


print(G.nodes[10])

print(nx.is_directed_acyclic_graph(G))

print(list(nx.topological_sort(G)))

print(G.nodes[6132])

weight_list = []
for i in range(len(data)):
    weight_list.append(G.nodes[i]['weight'])
print(weight_list)

print(data[43596]['hash'])
