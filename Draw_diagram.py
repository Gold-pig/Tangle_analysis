import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pylab as pl

with open("diff_list.json") as f:
    diff_list = json.load(f)
with open("diff_list_branch.json") as f:
    diff_list1 = json.load(f)
with open("diff_list_trunk.json") as f:
    diff_list2 = json.load(f)
with open("branch_link_2016.json") as f:
    branch_link = json.load(f)
with open("trunk_link_2016.json") as f:
    trunk_link = json.load(f)
with open("transactions_2016 with c_weight_correct.json") as f:
    data = json.load(f)


#draw in_degree pie
# in_degree_list = {0: 1, 1: 22833, 2: 13504, 3: 4136, 4: 1291, 5: 526, 6: 325, 7: 195, 8: 138, 9: 111, 10: 105, 11: 71, 12: 57, 13: 63, 14: 44, 15: 29, 16: 27, 17: 28, 18: 21, 19: 10, 20: 18, 21: 8, 22: 5, 23: 5, 24: 9, 25: 3, 26: 4, 27: 3, 28: 3, 29: 4, 30: 1, 31: 2, 32: 1, 33: 3, 34: 3, 36: 3, 37: 2, 39: 1, 43: 1, 49: 1, 52: 1, 53: 1, 108: 1}
#
# x = []
# y = []
#
# for i in in_degree_list.keys():
#     x.append(i)
# for j in in_degree_list.values():
#     y.append(j)
#
# fig = plt.figure()
# plt.pie(y,labels = x,autopct= '%1.2f%%' )
# plt.title("in_degree")
# pl.show()

#draw diff_list pie for every diff 1-max
# def all_list(arr):
#     result = {}
#     for i in set(arr):
#         result[i] = arr.count(i)
#     return result
#
# print(all_list(diff_list))
#
# amount_diff_list = all_list(diff_list)
#
# list_1_10 =[]
# list_10_100=[]
# list_100_1000=[]
# list_1000_max = []
# for i in amount_diff_list :
#     if 1<=i & i <=10 :
#         list_1_10.append(amount_diff_list[i])
#     elif 10<i & i <=100 :
#         list_10_100.append(amount_diff_list[i])
#     elif 100<i & i <=1000 :
#         list_100_1000.append(amount_diff_list[i])
#     elif 1000<i :
#         list_1000_max.append(amount_diff_list[i])


# print(sum(amount_diff_list))
# print(sum(list_1_10)/87193)
# print(sum(list_10_100)/87193)
# print(sum(list_100_1000)/87193)
# print(sum(list_1000_max)/87193)
#
# print(sum(list_1_10)+sum(list_10_100)+sum(list_100_1000)+sum(list_1000_max))
# print(len(diff_list))
# print(len(diff_list1))
# print(len(diff_list2))

# diff_list_range = {"1-10":69178,"10-100":14579,"100-1000":1910,"1000-":1526}
# Draw the pie graph of diff_list
# x = []
# y = []
#
# for i in all_list(diff_list).keys():
#     x.append(i)
# for j in all_list(diff_list).values():
#     y.append(j)
#
# fig = plt.figure()
# plt.pie(y,labels = x,autopct= '%1.2f%%' )
# plt.title("diff_list")
# pl.show()


#find out the diff >1000 and print out corresponding serial number
# for index,i in enumerate(diff_list1):
#     if i > 1000:
#         print(index,i)
# print("_____")
#
# print(".............................")
# for index,i in enumerate(diff_list2):
#     if i > 1000:
#         print(index,i)

# For example, pick out branch 40258th and find it is [40260,494], found out all node reference 494
# print(branch_link[40258])
#
# for i in branch_link:
#     if i[1] == 494:
#         print(i)
# for i in trunk_link:
#     if i[1] == 494:
#         print(i)
#
#
#
# print(data[494])
# print(data[493])
# print(data[40260])
# print(data[40261])
# print(data[40262])
# print(data[40263])
# print(data[40264])
# print(data[41112])
# print(data[41113])
# print(data[41114])
# print(data[41115])
# print(data[39527])
# print(data[40265])
# print(data[41116])

# find the branch has cumulative weight diff > 1000 and print corresponding
branch_index_bigger_1000 = []
for index, i in enumerate(diff_list1) :
    if i > 1000:
        branch_index_bigger_1000.append(index)

branch_link_bigger_1000 = []

for i in branch_index_bigger_1000:
    branch_link_bigger_1000.append(branch_link[i])

print(branch_link_bigger_1000)

print(len(branch_index_bigger_1000))


trunk_index_bigger_1000 = []
for index, i in enumerate(diff_list2) :
    if i > 1000:
        trunk_index_bigger_1000.append(index)

trunk_link_bigger_1000 = []
for i in trunk_index_bigger_1000:
    trunk_link_bigger_1000.append(trunk_link[i])

print(trunk_link_bigger_1000)

print(len(trunk_link_bigger_1000))

for i in branch_link_bigger_1000:
    print(data[i[1]]["timestampDate"])

for i in data :
    if i["cumulative weight"] == 43597:
        print(i)
print(data[0])
print(data[43597])

