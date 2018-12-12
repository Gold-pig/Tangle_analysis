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

G.add_node(10, weight=data[10]['cumulative weight'])

print(G.nodes[10])

print(list(nx.topological_sort(G)))

# print(list(nx.topological_sort(nx.line_graph(G))))
print(nx.number_of_edges(G))
print(len(branch_link))
print(len(trunk_link))
