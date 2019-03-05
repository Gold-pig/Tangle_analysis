import networkx as nx
import json

with open("IRI_1.1.2.4_18675.json") as f:
    data = json.load(f)
with open('trunk_link_IRI_1.1.2.4_18675.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_IRI_1.1.2.4_18675.json') as f2:
        branch_link = json.load(f2)

name = "MS3"

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)


milestone_num = {}
for i in range(len(data)):
    if data[i]["address"] ==  "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
        milestone_num[i] = int(data[i]["timestamp"])
# print(milestone_num)

sort_timestamp = sorted(milestone_num.items(), key= lambda  item:item[1])

milestone_sorted = []

for i in sort_timestamp:
    milestone_sorted.append(i[0])

print(milestone_sorted)


with open("{}_sort_timestamp.json".format(name),"w") as f:
    json.dump(milestone_sorted,f)


