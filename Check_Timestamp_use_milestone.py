import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import csv

#check  how many tx in one day between two milestone . 检测两个固定时间（一天）milesone之间有多少tx
with open("transactions_2016.json") as f:
    data = json.load(f)
with open("cw_6000.json") as f:
    cw_raw = json.load(f)

#For milestone, key = Timestamp value = Cumulative weight
mile_time_cw = {}
with open('MS1_mile_time_cw.csv') as f:
    mile_cw = csv.DictReader(f)
    for row in mile_cw:
        mile_time_cw[int(row["Timestamp"])] = int(row["Cumulative_weight"])

#For all, key: site num. , value = Cumulative weight
cw = {}
for items in cw_raw.items():
    cw[int(items[0])] = items[1]

for items in mile_time_cw.items():
    if (1477868340-120) < items[0] < (1477868340+120):
        print(items[1])

for items in mile_time_cw.items():
    if (1477868340-3600+86400) < items[0] < (1477868340+300+86400):
        print(items[1])
        print(0)

count = 0
for i in range(len(data)):
    if 1477868340<int(data[i]["timestamp"])<(1477868340+86400):
        count+=1
print(count)


count_mile = 0
for i in mile_time_cw.items():
    if 1477868340<i[0]<(1477868340+86400):
        count_mile+=1
print(count_mile)
