import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import seaborn as sns; sns.set()


with open("IRI_1.1.2.4_18675.json","r") as f:
    data = json.load(f)
with open("cw_18675.json","r") as f:
    cw_raw = json.load(f)

# timestamp dict: key=site value=timestamp
timestamp = {}
for i in range(len(data)):
    timestamp[i] = data[i]["timestamp"]

timestamp_0 = []
for item in timestamp.items():
    if item[1] == 0:
        timestamp_0.append(item[0])
for i in timestamp_0:
    timestamp.pop(i)

print(len(timestamp))

# cumulative weight dict: key= site value=cumulative
cw = {}
# for i in range(len(data)):
#     cw[i] = data[i]["cumulative weight"]+1
for items in cw_raw.items():
    cw[int(items[0])] = items[1]
#print(cw)
# sorted timestamp from small to big
sort_timestamp = sorted(timestamp.items(), key= lambda  item:item[1])
#print(sort_timestamp)

# x_axis = []
# for i in range(len(data)):
#     x_axis.append(int(sort_timestamp[i][1]))
#
# y_axis = []
# for i in range(len(data)):
#     y_axis.append(int(cw[sort_timestamp[i][0]]))
# print(y_axis)

x_axis = []
for item in sort_timestamp:
    x_axis.append(int(item[1]))

y_axis = []
for item in sort_timestamp:
    y_axis.append(int(cw[item[0]]))
#print(y_axis)



#write down in csv file
dataframe = pd.DataFrame({'Timestamp':x_axis,'Cumulative_weight':y_axis})
dataframe.to_csv("MS3_time_cw.csv",index=False,sep=',')

#draw plot
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.scatter(x_axis[0:1000],y_axis[0:1000])
# plt.show()


# df = pd.read_csv('MS3_time_cw.csv',usecols=['Timestamp', 'Cumulative_weight'])
# sns.jointplot(x='Timestamp', y='Cumulative_weight', data=df)
# plt.show()



