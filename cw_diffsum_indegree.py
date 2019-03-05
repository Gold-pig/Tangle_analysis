import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import math
from collections import defaultdict

#diffsum/indegree, 若两个点reference同一个点，两个边diff很大，则证明其中有个点不在mainTangle


name = "MS1"

with open('trunk_link_2016.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_2016.json') as f2:
        branch_link = json.load(f2)
with open("cw_6000.json","r") as f:
    cw_raw = json.load(f)

cw = {}
for items in cw_raw.items():
    cw[int(items[0])] = items[1]

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

#######calculate every site predecessor and save as .json #########
predecessor = {}
for i in list(G.nodes):
    print(i)
    precessor_list = list(G.predecessors(i))
    predecessor[i] = precessor_list
print(predecessor)
with open("{}_predecessor.json".format(name),"w") as f:
    json.dump(predecessor,f)
###################################################################

site_diff_sum = {}

for i in predecessor.items():
    diff = []
    for j in range(len(i[1])):
        diff.append(cw[int(i[0])]-cw[int(i[1][j])])
    site_diff_sum[i[0]] = sum(diff)


#key = site value = diff_sum/in-degree
sum_divide_indegree = {}
for i in site_diff_sum.items():
    if G.in_degree(int(i[0])) == 0:
        sum_divide_indegree[i[0]] = 0
    else:
        sum_divide_indegree[i[0]] = i[1]/(G.in_degree(int(i[0])))

with open("{}_sum_divide_indegree.json".format(name),"w") as f:
    json.dump(sum_divide_indegree,f)

print(sum_divide_indegree)
