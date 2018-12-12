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

# print(nx.density(G))

for i in range(len(data)):
    if G.in_degree(i) == 0:
        tail = i
        print("The tail is:",i)
        print("Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data[i]["timestamp"]))))
        print("Time:",int(data[i]["timestamp"]))

for i in range(len(data)):
    if G.out_degree(i) == 0:
        head = i
        print("The head is:",i)
        print("Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data[i]["timestamp"]))))
        print("Time:",int(data[i]["timestamp"]))

short_path_list = nx.shortest_path(G,source= tail ,target=head)

milestone = 0
node_999 = 0
for i in short_path_list:
    if data[i]["address"] == "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
        milestone+=1
    if data[i]["address"]== "999999999999999999999999999999999999999999999999999999999999999999999999999999999":
        node_999+=1

other = len(short_path_list)-milestone-node_999
print("From the tail to head:",len(short_path_list),"sites")
print("The milestone num.:",milestone)
print("The precent of milestone is:", milestone/len(short_path_list) *100,"%")
print("The address 999 num:",node_999)
print("The precent of 999 is:", node_999/len(short_path_list) *100,"%")
print("The other address :",len(short_path_list)-milestone-node_999)
print("The precent of other sites is:", other/len(short_path_list) *100,"%")

print(nx.dag_longest_path_length(G))
print(nx.antichains(G))




