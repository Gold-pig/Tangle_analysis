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

name = "MS1"

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)


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
# with open("{}_milestonenum_time.json".format(name),"w") as f:
#     json.dump(sort_timestamp,f)

#print(len(nx.ancestors(G,sort_timestamp[0][0])))

# print(nx.descendants(G,6130))


# print(type(nx.descendants(G,sort_timestamp[0][0])))
# print(type(sort_timestamp[1][0]))
# print(diff((nx.descendants(G,sort_timestamp[0][0])),(nx.descendants(G,sort_timestamp[1][0]))))

tx_per_mile_confirmed = {}

for i,j in enumerate(sort_timestamp):
    if i == 0:
        tx_per_mile_confirmed[0] = list(nx.descendants(G,sort_timestamp[0][0]))
        print("milestone {}".format(0),[nx.descendants(G,sort_timestamp[0][0])])
    # elif i == 1:
    #     tx_per_mile_confirmed[i] = diff((nx.descendants(G,sort_timestamp[0][0])),(nx.descendants(G,sort_timestamp[1][0])))
    #     tx_per_mile_confirmed[i].remove(6132)        #list.remove(xx)  return None!  directly change on the list
    #     print("milestone {}".format(1), tx_per_mile_confirmed[i])
    else:
        tx_per_mile_confirmed[i] = diff(list(nx.descendants(G,sort_timestamp[i-1][0])),list(nx.descendants(G,sort_timestamp[i][0])))
        tx_per_mile_confirmed[i].remove(sort_timestamp[i-1][0])
        print("milestone {}".format(i),tx_per_mile_confirmed[i])

with open("{}_tx_per_mile_confirmed.json".format(name),"w") as f:
     json.dump(tx_per_mile_confirmed,f)

    # tx_per_mile[i] = diff((nx.ancestors(G,sort_timestamp[i+1][0])),(nx.ancestors(G,sort_timestamp[i][0])))
    # if i < (len(sort_timestamp)-1):
    #     tx_per_mile_confirmed[i] = diff((nx.descendants(G,sort_timestamp[i][0])),(nx.descendants(G,sort_timestamp[i+1][0])))
    #     print("milestone", diff(list((nx.descendants(G,sort_timestamp[i][0]))),list((nx.descendants(G,sort_timestamp[i+1][0])))))
    # else:
    #     tx_per_mile_confirmed[i] = list(nx.descendants(G,sort_timestamp[i][0]))
# print(tx_per_mile_confirmed)
#
milestone_nodelist = {}
for i,j in enumerate(tx_per_mile_confirmed.items()):
    # print(j)
    milestone_nodelist[sort_timestamp[i][0]] = j[1]
print(milestone_nodelist)
#
#
# with open("{}_tx_per_mile_confirmed.json".format(name),"w") as f:
#      json.dump(tx_per_mile_confirmed,f)
#
with open("{}_tx_per_mile_confirmed_spe.json".format(name),"w") as f:
     json.dump(milestone_nodelist,f)


# print(nx.descendants(G,6132))
# print(nx.descendants(G,6131))
# print(nx.descendants(G,6130))
# print(nx.descendants(G,6129))
# print(nx.descendants(G,6128))
