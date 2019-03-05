import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import seaborn as sns; sns.set()

with open("transactions_2016.json") as f:
    data = json.load(f)
with open("cw_6000.json") as f:
    cw_raw = json.load(f)
with open("MS1_sum_divide_indegree.json","r") as f:
    sum_divide_indegree = json.load(f)

with open('trunk_link_2016.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_2016.json') as f2:
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

name = "MS1"

milestone_list = []
for i in range(len(data)):
    if data[i]["address"] == "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
        milestone_list.append(int(i))
# print(milestone_list)

cw = {}
for items in cw_raw.items():
    cw[int(items[0])] = items[1]

milestone_cw = {}  #key = milestone_site_num, value = cumulaitve weight
for i in milestone_list:
    milestone_cw[i] = cw[i]
# print(milestone_cw)


time_cw = {} # For milestone, key = timestamp, value = cw
for items in milestone_cw.items():
    time_cw[int(data[items[0]]["timestamp"])] = items[1]
# print(time_cw)

sort_timestamp = sorted(time_cw.items(), key= lambda  item:item[0]) #(milestone timestamp, cw), timestamp from small to big
# print(sort_timestamp)

###draw scatter plot use this one####
mile_cw_ordered = {}  # key = natural_num  value = diff bewtween milestone_cw
for i,j in enumerate(sort_timestamp):
    if i < (len(sort_timestamp)-1):
        mile_cw_ordered[int(i)] = (sort_timestamp[i][1]-sort_timestamp[i+1][1])
    else:
        mile_cw_ordered[int(i)] = sort_timestamp[i][1]
###
print(mile_cw_ordered)
# with open("MS1_diff_mile.json","w") as f:
#     json.dump(mile_cw_ordered,f)

time_milenum = {} # key = mile_num, value = timetamp
for i in milestone_list:
    time_milenum[i] = int(data[i]["timestamp"])
# print(time_milenum)

sort_time_milenum = sorted(time_milenum.items(), key= lambda  item:item[1]) #(milestone_num, timestamp), timestamp from small to big
# print(sort_time_milenum)

milenum_diff = {}  # key = milestone_num, value = cw diff
for i,j in enumerate(mile_cw_ordered.items()):
    milenum_diff[sort_time_milenum[i][0]] = j[1]
# print(milenum_diff)

with open("MS1_milenum_diff.json","w") as f :
    json.dump(milenum_diff,f)

diff_10 = []
for i in milenum_diff.items():
    if i[1] > 10:
        diff_10.append(i[0])
print(diff_10)

#new parameter: diffsum/indegree
for i in diff_10:
    print(sum_divide_indegree['{}'.format(i)])

sum_divide_indegree_list = []
for i in sum_divide_indegree.items():
    sum_divide_indegree_list.append(int(i[1]))
print("sum_divide_indegree_list")
print("max",max(sum_divide_indegree_list))
print("min",min(sum_divide_indegree_list))
print("mean",np.mean(sum_divide_indegree_list))     #pingjun
print("median",np.median(sum_divide_indegree_list)) #zhongwei
counts = np.bincount(sum_divide_indegree_list)
print("mode",np.argmax(counts))   #zhongshu


mile_diff_list = []
for i in milenum_diff.items():
    mile_diff_list.append(i[1])

# print(mile_diff_list)
print("mile_diff_list")
print("max",max(mile_diff_list))
print("min",min(mile_diff_list))
print("mean",np.mean(mile_diff_list))     #pingjun
print("median",np.median(mile_diff_list)) #zhongwei
counts = np.bincount(mile_diff_list)
print("mode",np.argmax(counts)) #zhongshu
plt.hist(mile_diff_list,bins="auto")
plt.yscale("log")
plt.xlabel("Milestone_cw_diff")
plt.ylabel("Milestone_amount")
plt.show()



#draw timestamp_cw plot
x_axis = []
for item in mile_cw_ordered.items():
    x_axis.append(item[0])

y_axis = []
for item in mile_cw_ordered.items():
    y_axis.append(item[1])

#save data in csv file
dataframe = pd.DataFrame({'milestone':x_axis,'tx_per_milestone':y_axis})
dataframe.to_csv("{n}_tx_per_milestone.csv".format(n = name),index=False,sep=',')

df = pd.read_csv('{n}_tx_per_milestone.csv'.format(n = name),usecols=['milestone', 'tx_per_milestone'])
df.tail()
print(df.tail())


#sns.jointplot(x='milestone', y='tx_per_milestone', data=df,)
# #sns.jointplot(x='x', y='y', data=df, kind='hex', size=(8))
# #sns.regplot(x='Timestamp', y='Cumulative_weight', data=df)
#
plt.scatter(x='milestone', y='tx_per_milestone', data=df,marker='.')
plt.xlabel("milestone")
plt.ylabel("tx_per_milestone")
plt.title('{n}'.format(n = name))
plt.show()
#plt.savefig("{}_mile_time_cw.png".format(name))






#delete ## used when no milenum_diff
# for i in mile_cw_ordered.items():
#     if i[1] > 100:
#         print(i[0])
# print(sort_timestamp[5609])
# print(sort_timestamp[5610])
# print(sort_timestamp[5611])
#
# for i in range(len(data)):
#     if data[i]["timestamp"] == "1479931704":
#         print(data[i]["hash"])
# for i in range(len(data)):
#     if data[i]["timestamp"] == "1479973424":
#         print(data[i]["hash"])

# print(cw)

