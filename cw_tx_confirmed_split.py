import networkx as nx
import json
import time
import sys

name = "MS3"

with open('trunk_link_IRI_1.1.2.4_18675.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_IRI_1.1.2.4_18675.json') as f2:
        branch_link = json.load(f2)

with open("{}_sort_timestamp.json".format(name)) as f:
    sort_timestamp =json.load(f)

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)


def diff(listA,listB):
    listC = list(set(listB).difference(set(listA)))
    return listC

tx_per_mile_confirmed = {}

# para = int(sys.argv[1])
para = 6
if para*1000 < len(sort_timestamp):
    for i in range(((para-1)*1000),(para*1000)):
        if i == 0:
            tx_per_mile_confirmed[0] = list(nx.descendants(G,sort_timestamp[i]))
            print("milestone {}".format(0),list(nx.descendants(G,sort_timestamp[i])))
        else:
            tx_per_mile_confirmed[i] = diff(list(nx.descendants(G,sort_timestamp[i-1])),list(nx.descendants(G,sort_timestamp[i])))
            tx_per_mile_confirmed[i].remove(sort_timestamp[i-1])
            print("milestone {}".format(i),tx_per_mile_confirmed[i])


    with open("{}_mile_confirmed_{i}_{j}.json".format(name).format(i=((para-1)*1000), j=(para*1000)), "w+") as f:
        json.dump(tx_per_mile_confirmed,f)


    milestone_nodelist = {}
    for i,j in enumerate(tx_per_mile_confirmed.items()):
        milestone_nodelist[sort_timestamp[i]] = j[1]
    print(milestone_nodelist)

    with open("{}_milestone_confirmed_{i}_{j}.json".format(i=((para-1)*1000), j=(para*1000)), "w+") as f:
        json.dump(tx_per_mile_confirmed,f)
else:
    for i in range(((para-1)*1000),len(sort_timestamp)):
            tx_per_mile_confirmed[i] = diff(list(nx.descendants(G,sort_timestamp[i-1])),list(nx.descendants(G,sort_timestamp[i])))
            tx_per_mile_confirmed[i].remove(sort_timestamp[i-1])
            print("milestone {}".format(i),tx_per_mile_confirmed[i])
    with open("{n}_mile_confirmed_{i}_{j}.json".format(n = name, i=((para-1)*1000), j=(len(sort_timestamp))), "w") as f:
            json.dump(tx_per_mile_confirmed,f)

    milestone_nodelist = {}
    for i,j in enumerate(tx_per_mile_confirmed.items()):
        milestone_nodelist[sort_timestamp[i]] = j[1]
    print(milestone_nodelist)

    with open("{n}_milestone_confirmed_{i}_{j}.json".format(n = name, i=((para-1)*1000), j=(len(sort_timestamp))), "w") as f:
        json.dump(milestone_nodelist,f)




# para = int(sys.argv[1])
# for i in sort_timestamp[((para-1)*10000):(para*10000)]:
#     n = len(list(nx.ancestors(G,i)))+1
#     c_w[i] = n
# print(c_w)
# with open("cw216223_confirmed_{i}_{j}.json".format(i=((para-1)*10000), j=(para*10000)), "w+") as f:
#         json.dump(c_w,f)


# with open("{}_tx_per_mile_confirmed.json".format(name),"w") as f:
#      json.dump(tx_per_mile_confirmed,f)





# with open("{}_tx_per_mile_confirmed.json".format(name),"w") as f:
#      json.dump(tx_per_mile_confirmed,f)
#
# with open("{}_tx_per_mile_confirmed_spe.json".format(name),"w") as f:
#      json.dump(milestone_nodelist,f)
