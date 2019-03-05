import networkx as nx
import json
import time
import sys

name = "MS1"

with open('trunk_link_2016.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_2016.json') as f2:
        branch_link = json.load(f2)

with open("{}_sort_timestamp.json".format(name)) as f:
    sort_timestamp =json.load(f)

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

tx_per_mile = {}

sort_timestamp_reverse = list(reversed(sort_timestamp))
print(sort_timestamp_reverse)


for i,j in enumerate(sort_timestamp_reverse):
    if i ==0:
        tx_per_mile[j] = list(nx.ancestors(G,j))
        for n in (list(nx.ancestors(G,j))):
            G.remove_node(n)
    else:
        mile_list = list(nx.ancestors(G,j))
        mile_list.remove(sort_timestamp_reverse[i-1])
        tx_per_mile[j] = mile_list
        for n in (list(nx.ancestors(G,j))):
            G.remove_node(n)
print(tx_per_mile)
print(len(tx_per_mile))

# with open("{}_tx_per_mile_spe_fast.json".format(name),"w") as f:
#     json.dump(tx_per_mile,f)

#
# tx_per_mile = []
#
# for i,j in enumerate(sort_timestamp):
#     mile_confirmed = {}
#     if i ==0:
#         mile_confirmed[j] = list(nx.descendants(G,j))
#         for n in (list(nx.descendants(G,j))):
#             G.remove_node(n)
#         tx_per_mile.append(mile_confirmed)
#         print(mile_confirmed)
#     else:
#         mile_list = list(nx.descendants(G,j))
#         mile_list.remove(sort_timestamp[i-1])
#         mile_confirmed[j] = mile_list
#         tx_per_mile.append(mile_confirmed)
#         for n in (list(nx.descendants(G,j))):
#             G.remove_node(n)
#         print(mile_confirmed)
# print(tx_per_mile)
#







