import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import math
from collections import defaultdict

#测试diff list中，一个边中后面点的属性，若两个点reference同一个点，两个边diff很大，则证明其中有个点不在mainTangle

with open("MS1_diff_amount.json","r") as f:
    diff_amount = json.load(f)
with open("MS1_diff_dict.json","r") as f:
    diff_dict = json.load(f)
# with open("transactions_2016.json","r") as f:
#     data = json.load(f)
with open("transactions_2016 with c_weight_correct.json","r") as f:
    data = json.load(f)
with open("MS1_predecessor.json","r") as f:
    predecessor = json.load(f)
with open("cw_6000.json","r") as f:
    cw_raw = json.load(f)

cw = {}
for items in cw_raw.items():
    cw[int(items[0])] = items[1]

tip_list = []
for i in diff_dict.get("1"):
    tip_list.append(i[0])
#print(sorted(set(tip_list)))

with open('trunk_link_2016.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_2016.json') as f2:
        branch_link = json.load(f2)
with open("transactions_2016 with c_weight_correct.json","r") as f:
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
#print(list(G.predecessors(392)))
# for i in nx.predecessor(G,0).values():
#     print(len(i))
# num = 0
# for i in list(G.predecessors(392)):
#     num = num+1
#     print("num",num)
#     print("diff 392- {}".format(i),data[392]["cumulative weight"]-data[i]["cumulative weight"])
#    print("{} address:".format(i),data[i]["address"])
# print(data[42464]["hash"])
# print(data[391]["address"])

#######calculate every site predecessor and save as .json #########
# predecessor = {}
# for i in list(G.nodes):
#     print(i)
#     precessor_list = list(G.predecessors(i))
#     predecessor[i] = precessor_list
# print(predecessor)
# print(predecessor.get(392))
# with open("MS1_predecessor.json","w") as f:
#     json.dump(predecessor,f)
###################################################################

site_diff_sum = {}

for i in predecessor.items():
    diff = []
    for j in range(len(i[1])):
        diff.append(cw[int(i[0])]-cw[int(i[1][j])])
    site_diff_sum[i[0]] = sum(diff)

# print(site_diff_sum)
# print(site_diff_sum.get("392"))
# print(G.in_degree(392))


# print(type(G.in_degree(392)))

#key = site value = diff_sum/in-degree
sum_divide_indegree = {}
for i in site_diff_sum.items():
    if G.in_degree(int(i[0])) == 0:
        continue
    else:
        sum_divide_indegree[i[0]] = i[1]/(G.in_degree(int(i[0])))
#print(sum_divide_indegree)

with open("MS1_sum_divide_indegree.json","w") as f:
    json.dump(sum_divide_indegree,f)


# plt.hist(sum_divide_indegree.values(),bins=range(1,500,10))
# plt.yscale("log")
# plt.show()
# print(sum_divide_indegree.get("392"))
# print(data[380])

#print(nx.degree_assortativity_coefficient(G))
#print(nx.average_neighbor_degree(G,source="out",target="out"))

#print(nx.dag_longest_path_length(G))
#print(nx.is_weakly_connected(G))
#print((nx.dominance_frontiers(G,0).items()))

diff_indegree100 = []
for items in sum_divide_indegree.items():
    if items[1] > 100:
        diff_indegree100.append(items[0])
print(diff_indegree100)

for i in diff_indegree100:
    print(data[int(i)]["timestampDate"])
    print(data[int(i)]["hash"])

print(data[0]["hash"])
