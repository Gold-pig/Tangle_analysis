import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math

with open("IRI_1.4.1.7_337541.json","r") as f:
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
for item in data:
    if (1515279600+0*86400)< int(item["timestamp"]) < (1515279600+(2)*86400):
        count_list.append(item)
print(count_list)



