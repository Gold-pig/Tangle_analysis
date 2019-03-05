import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import random

with open("IRI_1.1.4.3_61491.json","r") as f:
    data = json.load(f)

print(len(data))

#timestamp list
# time_list = []
# for i in range(len(data)):
#     time_list.append(int(data[i]["timestamp"]))
# time_list_sort = sorted(time_list)
#
# print(time_list_sort[0],time_list_sort[-1])

count_list = []
count_list1 = []
for item in data:
    if (1524952800+10*86400)< int(item["timestamp"]) < (1524952800+(11)*86400):
        count_list.append((item["hash"],item["timestampDate"]))
    if (1524952800+65*86400)< int(item["timestamp"]) < (1524952800+(66)*86400):
        count_list1.append((item["hash"],item["timestampDate"]))
list = random.sample(count_list,1000)
list1 = random.sample(count_list1,1000)
print(len(count_list))
print(len(count_list1))
#print(count_list)
print("=*=*=*=*=*=*=*=*=*===================")
#print(count_list1)
with open("check10_50.json","w") as f:
	json.dump(list,f)
with open("check10_120.json","w") as f:
	json.dump(list1,f)



