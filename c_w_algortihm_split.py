import matplotlib.pyplot as plt
import networkx as nx
import json
import time

with open('trunk_link_IRI_1.1.2.2_13157.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_IRI_1.1.2.2_13157.json') as f2:
        branch_link = json.load(f2)
with open("transactions_2016 with c_weight_correct.json") as f:
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

# milestone = []
# for i,j in enumerate(data):
#     if j["address"] == "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
#         milestone.append(i)
# print(milestone)
print(time.asctime( time.localtime(time.time())))

c_w = {}
for i in range(0,1000):
    n = len(list(nx.ancestors(G,i)))
    c_w[i] = n
print(c_w)
print(time.asctime( time.localtime(time.time()) )
)
for i in range(1000,2000):
    n = len(list(nx.ancestors(G,i)))
    c_w[i] = n
print(c_w)
print(time.asctime( time.localtime(time.time()) )
)
for i in range(48000,49000):
    n = len(list(nx.ancestors(G,i)))
    c_w[i] = n
print(c_w)
print(time.asctime( time.localtime(time.time()) )
)
# for i in range(5084,9533):
#     n = len(list(nx.ancestors(G,i)))
#     print(n)
#     c_w.append(n)


