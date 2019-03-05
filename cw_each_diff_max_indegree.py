import json
import pandas as pd
import networkx as nx
import json
import pandas as pd



name = "MS2"

with open("branch_link_IRI_1.1.2.2_13157.json") as f0:
    branch_link = json.load(f0)
with open("trunk_link_IRI_1.1.2.2_13157.json") as f1:
    trunk_link = json.load(f1)

with open("cw_13157.json") as f:
    cw_raw = json.load(f)
with open("{}_predecessor.json".format(name)) as f:
    predecessor = json.load(f)

cw = {}
for items in cw_raw.items():
    cw[int(items[0])] = items[1]

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

#site max diffierence
site_diff_max = {}

for i in predecessor.items():
    diff = []
    if i[1] ==[]:
        site_diff_max[int(i[0])] = 0
    else:
        for j in range(len(i[1])):
            diff.append(cw[int(i[0])]-cw[int(i[1][j])])
            site_diff_max[int(i[0])] = max(diff)

print(site_diff_max)
print(len(site_diff_max))

# with open("{}_site_diff_max.json".format(name),"w+") as f:
#     json.dump(site_diff_max,f)

site_diff_max_list = []
list1 = []
list2 = []
for i in site_diff_max.items():
    list1.append(int(i[0]))
    list2.append(i[1])
site_diff_max_list = (list1,list2)



##in-degree
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

dataframe = pd.DataFrame({'Site':list1,'Max_diff':list2,'In_degree':listb})
dataframe.to_csv("{}_site_diff_max_in_degree.csv".format(name),index=False,sep=',')
