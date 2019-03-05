import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import math
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

#identify the star structure
in_degree_list = []
for i in range(0,43598):
    in_degree_list.append(G.in_degree(i))

#find the sites wiht in_degree bigger than 10
In_degree_big_10 = []
for i in range(0,43598):
    if in_degree_list[i] > 10:
        In_degree_big_10.append(i)
print(In_degree_big_10)

milestone_num = 0
no_milestone_num = 0
for item in In_degree_big_10:
    if data[item]["address"] == 'KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU':
        milestone_num+=1
    else:
        no_milestone_num+=1
print("Milestone number:" ,milestone_num)
print("No Milestone number:",no_milestone_num)

# print(in_degree_list)
print("max in_degree:",max(in_degree_list))

# with open('In_degree_list_IRI.json', 'w') as f3:
#         f3.write(json.dumps(in_degree_list))
####Delete: find a node with in-degree 108
for i in range(len(data)):
    if G.in_degree(i) == 7:
        print(i)
        print(data[i]["hash"])
        print(data[i]['address'])
        for j in range(len(data)):
           if list(G.successors(j)).__contains__(i):
               print("Its children are ",j,data[j]["tag"])



# list_784 = []
# for i in range(len(branch_link)):
#     if branch_link[i][1] == 784:
#         list_784.append(branch_link[i])
# for i in range(len(trunk_link)):
#     if trunk_link[i][1] == 784:
#         list_784.append(trunk_link[i])
# print(len(list_784))
####

#counting function
# def all_list(arr):
#     result = {}
#     for i in set(arr):
#         result[i] = arr.count(i)
#     return result
#
# print(all_list(in_degree_list))
# in_degree_statistic = all_list(in_degree_list)
# print(len(in_degree_list))

#which in-degree has the most nodes
# print("--max and min indegree and nodes amount-- ")
# print("There are",max(in_degree_statistic.values()), " nodes have in-degree",max(in_degree_statistic,key=in_degree_statistic.get),", perscent is :" ,max(in_degree_statistic.values())/len(in_degree_list) )
# print("There are",min(in_degree_statistic.values()), " nodes have in-degree",min(in_degree_statistic,key=in_degree_statistic.get) )


print("Max in_degree:",max(in_degree_list),", node index is :",in_degree_list.index(max(in_degree_list)))
print("Mean is:",np.mean(in_degree_list))
print("Median is:",np.median(in_degree_list))

# draw in_degree pie

# x = []
# y = []
#
# for i in in_degree_statistic.keys():
#     x.append(i)
# for j in in_degree_statistic.values():
#     y.append(j)
#
# fig = plt.figure()
# # ax1 = fig.add_subplot(121)
# # plt.pie(y,labels = x,autopct= '%1.2f%%' )
# plt.title("IRI_1.5.5")
# plt.xlabel('degree num.')
# plt.ylabel('percent')
#dram histogram
# log_list = []
# for i in list(in_degree_statistic.values()):
#     log_list.append(math.log(i))

# print(log_list)
# ax2 = fig.add_subplot(122)
# plt.bar(in_degree_statistic.keys(),log_list, fc = 'b')
# plt.show()

#degree distribution
# print(nx.degree_histogram(G))
# degree =  nx.degree_histogram(G)          #返回图中所有节点的度分布序列
# x = range(len(degree))                             #生成x轴序列，从1到最大度
# # y = degree
# y = [z / float(sum(degree)) for z in degree]
# #将频次转换为频率，这用到Python的一个小技巧：列表内涵，Python的确很方便：）
# # ax3 = fig.add_subplot(122)
#
# plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线
#
#
# plt.show()                                                            #显示图表

#匹配性???
# print(nx.degree_assortativity_coefficient(G))

#centrality
# print(nx.closeness_centrality(G))

