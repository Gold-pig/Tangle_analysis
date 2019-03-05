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

name = "MS1"

milestone_list = []
for i in range(len(data)):
    if data[i]["address"] == "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
        milestone_list.append(int(i))

cw = {}
for items in cw_raw.items():
    cw[int(items[0])] = items[1]

milestone_cw = {}  #key = milestone_site_num, value = cumulaitve weight
for i in milestone_list:
    milestone_cw[i] = cw[i]

time_cw = {}
for items in milestone_cw.items():
    time_cw[int(data[items[0]]["timestamp"])] = items[1]

sort_timestamp = sorted(time_cw.items(), key= lambda  item:item[0])

print(sort_timestamp)
#draw timestamp_cw plot
x_axis = []
for item in sort_timestamp:
    x_axis.append(item[0])

y_axis = []
for item in sort_timestamp:
    y_axis.append(item[1])

#save data in csv file
dataframe = pd.DataFrame({'Timestamp':x_axis,'Cumulative_weight':y_axis})
dataframe.to_csv("{n}_mile_time_cw.csv".format(n = name),index=False,sep=',')

df = pd.read_csv('{n}_mile_time_cw.csv'.format(n = name),usecols=['Timestamp', 'Cumulative_weight'])
df.tail()
print(df.tail())


sns.jointplot(x='Timestamp', y='Cumulative_weight', data=df)
# #sns.jointplot(x='x', y='y', data=df, kind='hex', size=(8))
# #sns.regplot(x='Timestamp', y='Cumulative_weight', data=df)
#
# # plt.scatter(x='Timestamp', y='Cumulative_weight', data=df,marker='.')
# # plt.xlabel("Timestamp")
# # plt.ylabel("Cumulative_weight")
# plt.title('{n}'.format(n = name))
plt.show()
#plt.savefig("{}_mile_time_cw.png".format(name))
