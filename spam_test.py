import matplotlib.pyplot as plt
import networkx as nx
import json
import time
import datetime

with open("branch_link_2016.json") as f0:
    branch_link = json.load(f0)

with open("trunk_link_2016.json") as f1:
    trunk_link = json.load(f1)

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

spam = []
num = 0
mile = 0
mile_list=[]
for i1 in range(len(data)):
    if (''.join(data[i1]["tag"])).__contains__("SPAM") or (''.join(data[i1]["tag"])).__contains__("TOTALLY"):
        num+=1
        spam.append(i1)
for i2 in range(len(data)):
    if (''.join(data[i2]["address"])).__contains__("KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU"):
        mile+=1
        mile_list.append(i2)
print("spam:",num)
# print(spam)
print("milestone",mile)
in_degree = []
for i3 in mile_list:
    in_degree.append(G.in_degree(i3))
# print(in_degree)


influence = []
inf = 0
spam = dict.fromkeys(spam, True)
for link in G.edges:
    if (link[1] in spam) and (link[0] not in spam) :
            influence.append(link)
            inf+=1




# if (G.edges[i][1] == n for i in range(len(data)) for n in spam):
#     print

# for i in spam:
#     if (link[1] ==i for link in G.edges) and (link[0] !=j for link in G.edges for j in spam) :
#         inf+=1

print("spam influence:",inf)
# print(influence)
# print(len(G.edges))
# print(data[43191]["hash"])
with open("spam_influence_43598.json","w") as f:
    json.dump(influence,f)

