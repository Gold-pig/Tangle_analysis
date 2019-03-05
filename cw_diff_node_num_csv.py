import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import math
from collections import defaultdict

name = "MS4"

with open('trunk_link_IRI_1.1.4.3_61491.json') as f1:   # trunk link
        trunk_link = json.load(f1)
with open('branch_link_IRI_1.1.4.3_61491.json') as f2:  # branch link
        branch_link = json.load(f2)
with open("cw_61491.json","r") as f:        # cw
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

#differnece list of edges
#key = diff   value : edges
diff_list = []
diff_dict = defaultdict(list)
for edge in G.edges:
    diff_list.append(cw[edge[1]]-cw[edge[0]])
    diff_dict[int(cw[edge[1]]-cw[edge[0]])].append(edge)
# print(diff_list)
print(diff_dict)
print(len(diff_dict))
print(sorted(diff_dict.keys()))

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

diff_num = all_list(diff_list)
print(all_list(diff_list))
with open("{}_diff_amount.json".format(name),"w") as f:
    json.dump(all_list(diff_list),f)
x_axis = list(diff_num.keys())
y_axis = list(diff_num.values())

#save data in csv
dataframe = pd.DataFrame({'Difference':x_axis,'Sites amount':y_axis})
dataframe.to_csv("{}_diff_amount.csv".format(name),index=False,sep=',')


with open("{}_diff_dict.json".format(name),"w") as f:  #key = diff   value : edges
    json.dump(diff_dict,f)
