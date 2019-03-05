import json
from collections import defaultdict
import networkx as nx


name = "MS3"

with open("IRI_1.1.2.4_18675.json") as f:
    data = json.load(f)
with open("{n}_sort_timestamp.json".format(n = name)) as f:
    sort_timestamp =json.load(f)

with open("branch_link_IRI_1.1.2.4_18675.json") as f0:
    branch_link = json.load(f0)

with open("trunk_link_IRI_1.1.2.4_18675.json") as f1:
    trunk_link = json.load(f1)

#find the milestone with same bundle
G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)


#Method 1: use the raw data
# all_mile = []
# bundle_num = defaultdict(list)
# for i in range(len(data)):
#     if data[i]["address"] =="KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
#         bundle_num[data[i]['bundle_hash']].append(i)
#         all_mile.append(i)

#Method 2: use the timestamp list.
# all_mile = []
# for i in range(len(data)):
#     if data[i]["address"] == "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
#         all_mile.append(i)
# print("all_mile",len(all_mile))

bundle_num = defaultdict(list)
for i in sort_timestamp:
    bundle_num[data[i]["bundle_hash"]].append(i)
print(bundle_num)






reattach = []
for i in bundle_num.items():
    if len(i[1]) > 1:
        reattach.append(i[1])

#Find the real mile and fake milestone.
#Method 1: Seams not work
# real_mile = []
# for i in reattach:
#     for j in i[1]:
#         if sort_timestamp.__contains__(G.predecessors(j)) or sort_timestamp.__contains__(G.successors(j)):
#             real_mile.append(j)
#
# print(real_mile)

#Method 2: Find the real miletone: real milestone connects with each other
real_mile = []
for i in reattach:
    for j in i[1]:
        successors = list(G.successors(j))
        predecessors = list(G.predecessors(j))
        for n in successors:
            if sort_timestamp.__contains__(n):
                real_mile.append(j)
        for m in predecessors:
            if sort_timestamp.__contains__(m):
                real_mile.append(j)


print(real_mile)







# print(bundle_num)
# print(reattach)


#
# same_bundles = {}
# for i in sort_timestamp:
#     same_bundle = []
#     for j in sort_timestamp:
#         if data[i]["bundle_hash"] == data[j]['bundle_hash'] and i != j:
#             same_bundles[i] = j
# print(same_bundles)








