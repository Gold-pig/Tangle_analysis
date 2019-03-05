import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import seaborn as sns; sns.set()
import time

with open("transactions_2016.json") as f:
    data = json.load(f)
with open("cw_6000.json") as f:
    cw_raw = json.load(f)
with open('trunk_link_2016.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_2016.json') as f2:
        branch_link = json.load(f2)

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

name = "MS1"

def diff(listA,listB):
    listC = list(set(listB).difference(set(listA)))
    return listC

milestone_num = {}
for i in range(len(data)):
    if data[i]["address"] ==  "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
        milestone_num[i] = int(data[i]["timestamp"])
# print(milestone_num)

sort_timestamp = sorted(milestone_num.items(), key= lambda  item:item[1])

print(sort_timestamp)
with open("{}_milestonenum_time.json".format(name),"w") as f:
    json.dump(sort_timestamp,f)

#print(len(nx.ancestors(G,sort_timestamp[0][0])))



tx_per_mile = {}
for i in range(len(sort_timestamp)):
    if i < (len(sort_timestamp)-1):
        tx_per_mile[i] = diff((nx.ancestors(G,sort_timestamp[i+1][0])),(nx.ancestors(G,sort_timestamp[i][0])))
        print("milestone", diff(list((nx.ancestors(G,sort_timestamp[i+1][0]))),list((nx.ancestors(G,sort_timestamp[i][0])))))
    else:
        tx_per_mile[i] = list(nx.ancestors(G,sort_timestamp[i][0]))
print(tx_per_mile)

milestone_nodelist = {}
for i,j in enumerate(tx_per_mile):
    milestone_nodelist[sort_timestamp[i][0]] = j[1]


with open("{}_txs_per_milestone.json".format(name),"w") as f:
     json.dump(tx_per_mile,f)

with open("{}_txs_per_milestone_spe.json".format(name),"w") as f:
     json.dump(milestone_nodelist,f)


