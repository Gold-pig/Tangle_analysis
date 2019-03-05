# import matplotlib.pyplot as plt
import networkx as nx
import json
import pandas as pd


name = "MS1"

with open("branch_link_2016.json") as f0:
    branch_link = json.load(f0)

with open("trunk_link_2016.json") as f1:
    trunk_link = json.load(f1)

# with open("transactions_2016 with c_weight_correct.json") as f:
#     data = json.load(f)

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

in_degree_dict = {}
for i in G.nodes:
    in_degree_dict[i] = G.in_degree(i)
print(in_degree_dict)
with open("{}_indegree_dict.json".format(name),"w") as f:
    json.dump(in_degree_dict,f)

lista = []
listb = []
for i in in_degree_dict.items():
    lista.append(i[0])
    listb.append(i[1])


dataframe = pd.DataFrame({'Site':lista,'In_degree':listb,""})
dataframe.to_csv("{}_indegree_dict.csv".format(name),index=False,sep=',')
