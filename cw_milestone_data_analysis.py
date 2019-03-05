import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import seaborn as sns; sns.set()
from scipy.stats import mode


with open("MS1_diff_mile.json","r") as f:
    diff_mile = json.load(f)
with open("MS1_milenum_diff.json","r") as f :
    milenum_diff = json.load(f)
with open("MS1_txs_per_milestone.json") as f:
    txs_per_mile = json.load(f)
with open("MS1_milestone_nodelist.json") as f:
    mile_nodelist = json.load(f)


with open("MS1_sum_divide_indegree.json") as f:
    sum_divide_indegree = json.load(f)

with open("diff_list.json","r") as f:
    diff_list = json.load(f)

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

mile_diff_list = []
for i in diff_mile.items():
    mile_diff_list.append(i[1])
# print(mile_diff_list)

#count the amount for every diff
def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result
# print(all_list(mile_diff_list))
# print(all_list(diff_list))
# print(milenum_diff)
# print(sum_divide_indegree["6132"])

mile_diffsum_indegree = {}
for i in milenum_diff.items():
    if i[0] != "0":
        mile_diffsum_indegree[i[0]] = sum_divide_indegree[i[0]]
# print(mile_diffsum_indegree)
# print(mile_diffsum_indegree.values())
mile_diffsum_indegree_list = mile_diffsum_indegree.values()
print("mile_diff_divide_indegree_list")
print("max",max(list(mile_diffsum_indegree_list)))
print("min",min(list(mile_diffsum_indegree_list)))
print("mean",np.mean(list(mile_diffsum_indegree_list)))     #pingjun
print("median",np.median(list(mile_diffsum_indegree_list))) #zhongwei
print("mode",mode(list(mile_diffsum_indegree_list))) #zhongshu

# plt.hist(list(mile_diffsum_indegree_list))
# plt.yscale("log")
# plt.xlabel("Milestone_cw_diff_indegree")
# plt.ylabel("Milestone_amount")
# plt.show()

#The biggest diffsum/indegree
for i in mile_diffsum_indegree.items():
    if i[1] == 2375.75:
        print(i)

print(milenum_diff['666'])
print(data[666])

print(list(nx.neighbors(G,666)))
print(list(G.predecessors(666)))
print(cw_raw['666'])
for i in list(G.predecessors(666)):
    print("{}".format(i),cw_raw['{}'.format(i)])

print(data[39167]["address"])
print(data[665]["address"])

print(list(G.predecessors(42162)))
print(list(G.predecessors(42161)))
print(data[42161]["hash"])
print(list(G.predecessors(42160)))
print(data[42160]["hash"])
print(list(G.predecessors(42159)))
print(data[42159]["hash"])
print(cw_raw['42162'])
print(cw_raw['42161'])
print(cw_raw['42160'])
print(cw_raw['42159'])
print(cw_raw['42158'])
print(cw_raw['42157'])

for i in mile_nodelist.items():
    if i[1].__contains__(42157):
        print(i)
print(data[666]["hash"])
print(data[665]["hash"])
print(data[664]["hash"])
print(data[663]["hash"])
print(data[662]["hash"])
print(data[661]["hash"])
print(data[660]["hash"])

#GUJ9OYYYKLHTKYHNUNB9WAZXJQZIVVBHAYAWRZSDVENUQDOGQILRKVONRWHJPBXVPXIUBWMQLNB999999

for i in range(len(data)):
    if data[i]["hash"] == 'GUJ9OYYYKLHTKYHNUNB9WAZXJQZIVVBHAYAWRZSDVENUQDOGQILRKVONRWHJPBXVPXIUBWMQLNB999999':
        print(i)

# print(nx.ancestors(G,42179))
# print(list(G.predecessors(42179)))


ancestor42179__list = list(nx.ancestors(G,42179))
ancestor42179__mile_list = []  # Assume: ancestors successors attach to milestone
for i in ancestor42179__list:
    if data[int(i)]["address"] == 'KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU':
        ancestor42179__mile_list.append(i)
print(ancestor42179__mile_list)

mile_order_list = []
for i in milenum_diff.items():
    mile_order_list.append(int(i[0]))
print(mile_order_list)

print(data[394])
ancestor42179__diffsum_indegree_list = {}
for i in ancestor42179__list:
    if i != 0:
        ancestor42179__diffsum_indegree_list[i] = sum_divide_indegree["{}".format(i)]
print(ancestor42179__diffsum_indegree_list)   # most of them are 1. until to the first milestone.


print(data[43544])

ancestor42179_successors = {}
for i in ancestor42179__list:
    ancestor42179_successors[int(i)] = list(G.successors(i))
print(ancestor42179_successors)




print(len(ancestor42179_successors))
print(nx.shortest_path(G,source = 394, target=42179 ))
print("shortest path length",len(nx.shortest_path(G,source = 394, target=42179 )))
print("Amount of ancestors",len(ancestor42179__list))

print(data[42179]["hash"]) #  thetangle.com show confirmation time
print(data[39747]["hash"])
print(data[394]["hash"])
print(data[395]["hash"])
