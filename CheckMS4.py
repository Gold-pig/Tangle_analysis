import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math

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
    if (1486162800+10*86400)< int(item["timestamp"]) < (1486162800+(11)*86400):
        count_list.append(item["hash"])
    if (1486162800+100*86400)< int(item["timestamp"]) < (1486162800+(101)*86400):
        count_list1.append(item["hash"])
print(len(count_list))
print(len(count_list1))
print(count_list)
print("=*=*=*=*=*=*=*=*=*===================")
print(count_list1)



