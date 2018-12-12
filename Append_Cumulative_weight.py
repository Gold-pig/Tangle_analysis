import matplotlib.pyplot as plt
import networkx as nx
import json

#convert .json to list
with open('trunk_link_IRI_1.0.2_110916.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_IRI_1.0.2_110916.json') as f2:
        branch_link = json.load(f2)

with open("transactions_2016.json") as f:
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



#test for cumulative weight list
cum_weight_list = []
for i in range(len(data)):
        n = len(nx.ancestors(G,i))
        cum_weight_list.append(n)
print(cum_weight_list)

#test for add the cumulative weight to the original dataset
new_database = []
for i in range(len(data)):
        data[i].setdefault('cumulative weight',cum_weight_list[i]+1)
        print(data[i])
        new_database.append(data[i])
print(new_database)



with open('transactions_2016 with c_weight_test.json', 'w') as f3:
        f3.write(json.dumps(new_database))

# in_degree_list = []
# for i in range(0,468376):
#     in_degree_list.append(G.in_degree(i))
#
# with open('In_degree_list_2016', 'w') as f3:
#         f3.write(json.dumps(in_degree_list))


