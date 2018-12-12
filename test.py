import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pylab as pl
# G_tmp = nx.DiGraph()
# links = [(1,0),(2,0),(3,2),(4,2),(5,4),(6,4)]
# for link in links:
#   G_tmp.add_edge(link[0], link[1])
#
# weight_list = []
# for i in [0,1,2,3,4,5,6]:
#     w = len(nx.ancestors(G_tmp,i)) + 1
#     weight_list.append(w)
# print(weight_list)
#
# diff = []
# for i in range(len(links)):
#     dif = weight_list[links[i][1]] - weight_list[links[i][0]]
#     diff.append(dif)
# print(diff)

# c_w = []
#
# with open("transactions_2016 with c_weight_correct.json") as f:
#     data = json.load(f)
#
# for i in range(len(data)):
#     c_w.append(data[i]['cumulative weight'])
# c5 = []
# for i in c_w:
#     if i> 5000:
#         c5.append(i)
#
# print(len(c5))
# print(c5)


# dict = {0: 1, 1: 22833, 2: 13504, 3: 4136, 4: 1291, 5: 526, 6: 325, 7: 195, 8: 138, 9: 111, 10: 105, 11: 71, 12: 57, 13: 63, 14: 44, 15: 29, 16: 27, 17: 28, 18: 21, 19: 10, 20: 18, 21: 8, 22: 5, 23: 5, 24: 9, 25: 3, 26: 4, 27: 3, 28: 3, 29: 4, 30: 1, 31: 2, 32: 1, 33: 3, 34: 3, 36: 3, 37: 2, 39: 1, 43: 1, 49: 1, 52: 1, 53: 1, 108: 1}
# value = list(dict.values())
# # keys = list(dict.keys())
# with open("degree_list_IRI_1.1.0.json") as f:
#     data = json.load(f)
# bins = [0,10,20,30,40,50,60,70,80,90,100,110]
#
# # bins = 5
#
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
#
# ax.set_yscale('log')
#
# plt.hist(data,bins,rwidth=0.8)
# plt.title("S2")
# plt.xlabel('In_degree num.')
# plt.ylabel('nodes num. ')
# plt.legend()
# plt.show()


# with open("branch_link_2016.json") as f0:
#     branch_link = json.load(f0)
#
# with open("trunk_link_2016.json") as f1:
#     trunk_link = json.load(f1)

with open("IRI_1.4.2.2_426522.json") as f:
    data = json.load(f)

# G = nx.DiGraph()
#
# for e in range(len(trunk_link)):
#     a = trunk_link[e][0]
#     b = trunk_link[e][1]
#     G.add_edge(a, b)
# for e in range(len(branch_link)):
#     a = branch_link[e][0]
#     b = branch_link[e][1]
#     G.add_edge(a, b)

# print(list(G.predecessors(123)))
# print(G.in_degree(123))
# print(G.out_degree(123))
print(data[20499])
