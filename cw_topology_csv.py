import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import seaborn as sns; sns.set()


# with open('trunk_link_2016.json') as f1:
#         trunk_link = json.load(f1)
# with open('branch_link_2016.json') as f2:
#         branch_link = json.load(f2)
# with open("transactions_2016 with c_weight_correct.json","r") as f:
#         data = json.load(f)
with open('topology_18675.json') as f:
        topology = json.load(f)
with open("cw_18675.json","r") as f:
    cw_raw = json.load(f)

name = "MS3"

# cumulative weight dict: key= site value=cumulative
# cw = {}
# for i in range(len(data)):
#     cw[i] = data[i]["cumulative weight"]+1
# for items in cw_raw.items():
#    cw[int(items[0])] = items[1]

x_axis = []
x_axis = topology

y_axis = []
# for i in topology:
#     y_axis.append(int(data[i]["cumulative weight"]+1))

# cumulative weight dict: key= site value=cumulative
cw = {}
# for i in range(len(data)):
#     cw[i] = data[i]["cumulative weight"]+1
for items in cw_raw.items():
    cw[int(items[0])] = items[1]

for i in topology:
    y_axis.append(cw[i]) # dict[key] = value

# delete 0 timestamp
# for i in y_axis:
#     if i ==0:
#         y_axis.remove(0)

print(len(y_axis))
order = []
for i in range(len(y_axis)):
    order.append(i+1)
print(order)


#write down in csv file
dataframe = pd.DataFrame({'topology_sort':topology,'Topology_order':order,'Cumulative_weight':y_axis})
dataframe.to_csv("{n}_topology_order_cw.csv".format(n = name),index=False,sep=',')
#
#
#
df = pd.read_csv('{n}_topology_order_cw.csv'.format(n = name),usecols=['Topology_order', 'Cumulative_weight'])
df.tail()
print(df.tail())
plt.scatter(x='Topology_order', y='Cumulative_weight', data=df,marker='x')
plt.xlabel("Topology_order")
plt.ylabel("Cumulative_weight")
#sns.jointplot(x='Topology_order', y='Cumulative_weight', data=df)
plt.title('{n}'.format(n = name))
plt.show()
# plt.savefig('{n}_topology_order_cw.png'.format(n = name))

