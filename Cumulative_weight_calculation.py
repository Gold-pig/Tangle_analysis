# import matplotlib.pyplot as plt
# import networkx as nx
# import json
#
#
# G_tmp = nx.DiGraph()
# links = [(1,0),(2,0),(3,2),(4,2),(5,4),(6,4)]
# for link in links:
#   G_tmp.add_edge(link[0], link[1])
#
#
# # write by Jiahui
# precessors = dict()
# for e in G_tmp.edges():
# #for e in G.edges():
#   if e[1] not in precessors:
#     precessors[e[1]] = [e[0]]
#   else:
#     precessors[e[1]].append(e[0])
#
# for v in G_tmp.nodes():
# #for v in G.edges():
#   if v not in precessors:
#     precessors[v] = []
#
#
# print(precessors[0])
# root_idx = (min(G_tmp.out_degree(), key=lambda t: t[1]))[0]
#
# min_index = min(G_tmp.out_degree(), key=lambda t:t[1])[0]
# mins = [t[0] for t in G_tmp.in_degree() if t[1]==0]
# print("min_index:", mins)
# print(precessors[root_idx])
# weights = dict()
# def tag_precessors(idx):
#   c_pre = precessors[idx]
#   for p_idx in c_pre:
#     if p_idx not in weights:
#       weights[p_idx] = tag_precessors(p_idx)
#
#   weights[idx] = sum([weights[p_idx] for p_idx in c_pre]) + 1
#   return weights[idx]
#
# for v in G_tmp.nodes():
# #for v in G.nodes():
#   tag_precessors(v)
#
# print(weights)

import matplotlib.pyplot as plt
import networkx as nx
import json


G_tmp = nx.DiGraph()
# links = [(1,0),(2,0),(3,2),(4,2),(5,4),(6,4),(3,1)]
# for link in links:
#   G_tmp.add_edge(link[0], link[1])
#
# print(G_tmp.predecessors(0))

with open("branch_link_2016.json") as f0:
    branch_link = json.load(f0)

with open("trunk_link_2016.json") as f1:
    trunk_link = json.load(f1)

# with open("transactions_2016 with c_weight_correct.json") as f:
#      data = json.load(f)


for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G_tmp.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G_tmp.add_edge(a, b)



# G_tmp = nx.DiGraph()
# links = [(1,0),(2,0),(3,2),(4,2),(5,4),(6,4),(3,1)]
# for link in links:
#   G_tmp.add_edge(link[0], link[1])

print(G_tmp.predecessors(0))

# write by Jiahui
precessors = dict()
for e in G_tmp.edges():
#for e in G.edges():
  if e[1] not in precessors:
    precessors[e[1]] = [e[0]]
  else:
    precessors[e[1]].append(e[0])

for v in G_tmp.nodes():
  if v not in precessors:
    precessors[v] = []


print(precessors[0])
root_idx = (min(G_tmp.out_degree(), key=lambda t: t[1]))[0]

min_index = min(G_tmp.out_degree(), key=lambda t:t[1])[0]
mins = [t[0] for t in G_tmp.in_degree() if t[1]==0]
print("min_index:", mins)
print(precessors[root_idx])
print("root_idx:", root_idx)

weights = dict()
pcs = dict()
tagged = dict()
# def tag_precessors(idx):
#   c_pre = precessors[idx]
#   for p_idx in c_pre:
#     if p_idx not in weights:
#       weights[p_idx] = tag_precessors(p_idx)

#   weights[idx] = sum([weights[p_idx] for p_idx in c_pre]) + 1
#   return weights[idx]

# def tag_precessors(idx):
#   # print(idx)

#     if len(precessors[idx])==0:
#       # print(idx)
#       weights[idx] = 1
#       return {idx}
#     else:
#       pcs = {idx}
#       for p_idx in precessors[idx]:
#         # print(tag_precessors(p_idx))
#         pcs = pcs.union(tag_precessors(p_idx))
#         weights[idx] = len(pcs)
#       return pcs

def tag_precessors(idx):
  # pcs[idx] = {idx}
  # for p_idx in precessors[idx]:
  #   if p_idx not in tagged:
  #     pcs[p_idx] = tag_precessors(p_idx)
  #     tagged[p_idx] = 1
  #   pcs[idx] = pcs[idx].union(pcs[p_idx])
  # tagged[idx] = 1
  # return pcs[idx]
  if idx in pcs:
    return pcs[idx]
  else:
    pcs[idx] = {idx}
    for p_idx in precessors[idx]:
      if p_idx not in tagged:
        pcs[p_idx] = tag_precessors(p_idx)
      pcs[idx] = pcs[idx].union(pcs[p_idx])
      tagged[idx] = 1
    return pcs[idx]




for v in G_tmp.nodes():
  tag_precessors(v)

for i in pcs:
  weights[i] = len(pcs[i])
print(weights)
print(pcs)
