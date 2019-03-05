import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import seaborn as sns; sns.set()
from scipy.stats import mode

name = "MS3"

# with open("MS1_diff_mile.json","r") as f:
#     diff_mile = json.load(f)
# with open("MS1_milenum_diff.json","r") as f :
#     milenum_diff = json.load(f)
# with open("MS1_txs_per_milestone.json") as f:
#     txs_per_mile = json.load(f)
# with open("MS1_milestone_nodelist.json") as f:
#     mile_nodelist = json.load(f)

with open("MS3_tx_per_mile_confirmed.json") as f:
    txs_per_mile = json.load(f)
with open("MS3_tx_per_mile_confirmed_spe.json") as f:
    mile_nodelist = json.load(f)


# with open("MS1_sum_divide_indegree.json") as f:
#     sum_divide_indegree = json.load(f)
#
# with open("diff_list.json","r") as f:
#     diff_list = json.load(f)

# with open("transactions_2016.json") as f:
#     data = json.load(f)
with open("cw_18675.json") as f:
    cw_raw = json.load(f)

with open('trunk_link_IRI_1.1.2.4_18675.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_IRI_1.1.2.4_18675.json') as f2:
        branch_link = json.load(f2)


G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)


diff_mile = {}          #key = mile_order(0,1,2,...)  value = amount of confirmed tx
for i in txs_per_mile.items():
    diff_mile[i[0]] = len(i[1])
print(diff_mile)
#
#
# mile_diff_list = []     # amount of confirmed txs for each milestone
# for i in diff_mile.items():
#     mile_diff_list.append(i[1])
# # print(mile_diff_list)
#
# milenum_diff = {}       #key = mile_num, value = amount of its confirmed txs.
# for i in mile_nodelist.items():
#     milenum_diff[i[0]] = len(i[1])
# print(milenum_diff)
#
# amount_list = []   # list of amount of txs confirmed per milestone
# for i in diff_mile.items():
#     amount_list.append(i[1])
# print(amount_list)
#
#
# #count the amount for every diff
# def all_list(arr):
#     result = {}
#     for i in set(arr):
#         result[i] = arr.count(i)
#     return result
# # print(all_list(mile_diff_list))
# # print(all_list(diff_list))
# # print(milenum_diff)
# # print(sum_divide_indegree["6132"])
#
# # mile_diffsum_indegree = {}
# # for i in milenum_diff.items():
# #     if i[0] != "0":
# #         mile_diffsum_indegree[i[0]] = sum_divide_indegree[i[0]]
# # # print(mile_diffsum_indegree)
# # # print(mile_diffsum_indegree.values())
# # mile_diffsum_indegree_list = mile_diffsum_indegree.values()
# # print("mile_diff_divide_indegree_list")
# # print("max",max(list(mile_diffsum_indegree_list)))
# # print("min",min(list(mile_diffsum_indegree_list)))
# # print("mean",np.mean(list(mile_diffsum_indegree_list)))     #pingjun
# # print("median",np.median(list(mile_diffsum_indegree_list))) #zhongwei
# # print("mode",mode(list(mile_diffsum_indegree_list))) #zhongshu
#
# #Statistic for amount of txs confirmed per milestone
# print('{n}_txs_amount_per_milestone_confirmed'.format(n = name))
# print("max",max(list(amount_list)))
# print("min",min(list(amount_list)))
# print("mean",np.mean(list(amount_list)))     #pingjun
# print("median",np.median(list(amount_list))) #zhongwei
# print("mode",mode(list(amount_list))) #zhongshu
#
# # Plot: Histogram, mile_txs_amount--milestone amount
amount_list = []
for i in diff_mile.items():
    amount_list.append(i[1])
print(amount_list)
plt.figure()
plt.hist(amount_list,bins=100)
plt.yscale("log")
plt.title('{n}_txs_amount_per_milestone_confirmed'.format(n = name))
plt.xlabel("Amount of txs confirmed per milestone")
plt.ylabel("Amount of milestone")
# plt.savefig('{n}_txs_amount_per_milestone_confirmed.png'.format(n = name))

# Plot: milestone(in order list, 0,1,2....) -- amount of txs confirmed per milestone

x_axis = []
for item in diff_mile.items():
    x_axis.append(item[0])

y_axis = []
for item in diff_mile.items():
    y_axis.append(item[1])
#
# #save data in csv file
dataframe = pd.DataFrame({'milestone_order':x_axis,'tx_per_milestone_confirmed':y_axis})
dataframe.to_csv("{n}_tx_per_milestone_confirmed_order123.csv".format(n = name),index=False,sep=',')

df = pd.read_csv('{n}_tx_per_milestone_confirmed_order123.csv'.format(n = name),usecols=['milestone_order', 'tx_per_milestone_confirmed'])
df.tail()
print(df.tail())
#
#
# #sns.jointplot(x='milestone', y='tx_per_milestone', data=df,)
# # #sns.jointplot(x='x', y='y', data=df, kind='hex', size=(8))
# # #sns.regplot(x='Timestamp', y='Cumulative_weight', data=df)
# #
plt1.figure()
plt1.scatter(x='milestone_order', y='tx_per_milestone_confirmed', data=df,marker='.')
plt1.xlabel("milestone")
plt1.ylabel("tx_per_milestone_confirmed")
plt1.yscale("log")
plt1.title('{n}_txs_per_milestone_confirmed'.format(n = name))
plt1.savefig('{n}_txs_per_milestone_confirmed.png'.format(n = name))

