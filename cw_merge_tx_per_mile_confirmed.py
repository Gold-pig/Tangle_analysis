import json
import time
import sys

MS4 = {}
MS5 = {}
MS6 = {}
MS7 = {}
MS11 = {}
for n in range(1,43):
    with open("MS4_mile_confirmed_{i}_{j}.json".format(i =1000*(n-1) , j = 1000*n),"r") as f:
        data1 = json.load(f)
    for key,value in data1.items():
        MS4[key] = value

with open("MS4_mile_confirmed_42000_42741.json") as f:
    data1 = json.load(f)
for key,value in data1.items():
    MS4[key] = value



# for n in range(1,501):
#     with open("cw774804_{i}_{j}.json".format(i =1000000+2000*(n-1) , j =1000000+2000*n),"r") as f:
#         data2 = json.load(f)
#     for key,value in data2.items():
#         cw774804[key] = value
#
# for n in range(1,242):
#     with open("cw774804_{i}_{j}.json".format(i =2000000+1000*(n-1) , j =2000000+1000*n),"r") as f:
#         data2 = json.load(f)
#     for key,value in data2.items():
#         cw774804[key] = value
#
# with open("cw774804_2241000_2241877.json", "r") as f:
#     data3 = json.load(f)
#     for key,value in data3.items():
#         cw774804[key] = value
#
#
with open("MS4_tx_per_mile_confirmed.json","w") as f:
    json.dump(MS4,f)
# print(len(cw774804))
