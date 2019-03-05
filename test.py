import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pylab as pl
from networkx import nx
import numpy as np
import json
from operator import __or__, itemgetter
from functools import reduce
import random
from scipy import sparse
import time




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
#
#
# with open("branch_link_IRI_1.5.3_774804.json") as f0:
#     branch_link = json.load(f0)
#
# with open("trunk_link_IRI_1.5.3_774804.json") as f1:
#     trunk_link = json.load(f1)
# with open("topology_216223.json") as f1:
#     topology = json.load(f1)

# with open("IRI_1.4.2.2_426522.json") as f:
#     data = json.load(f)

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
# print(G.edges)

# print(list(G.predecessors(123)))
# print(G.in_degree(123))
# # print(G.out_degree(123))
# print(data[20499])
# data = [1] *len(G.edges)
# print(data)
# idxs = list(map(itemgetter(0), sorted((n, i) for i, n in enumerate(G.nodes))))

# A = sparse.lil_matrix((3528643,3528643))
# for i in G.edges:
#     A[i[0],i[1]] = 1
# print(A)

# B = nx.adjacency_matrix(G).todense
# print(B)

# print(nx.dfs_predecessors(G_tmp, source=6))
# list = list(nx.topological_sort(G))
# with open("topology_774804.json", "w+") as f:
#         json.dump(list,f)
# #
# print(time.asctime( time.localtime(time.time())))

# c_w = {}
# for i in topology[1077000:]:
#     n = len(list(nx.ancestors(G,i)))
#     c_w[i] = n
# print(c_w)
# with open("cw_1077000_1077960_587745.json", "w+") as f:
#         json.dump(c_w,f)
# print(time.asctime( time.localtime(time.time()) )
# )


def diff(listA,listB):
    listC = list(set(listB).difference(set(listA)))
    return listC
listA = [1,2,3,4]
listB = [1,2,3,4,5]
print(diff(listA,listB))
d = {}
d[1] = diff(listA,listB)
print(d)
