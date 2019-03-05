#2019-1-6 7.15pm
import matplotlib.pyplot as plt
import json
import os

names = locals()
folder = './'
counter = 1
timestamp = []
#open the json files in folder
for file in sorted(os.listdir(folder)):
    if file.endswith(".json"):
        with open(folder + file,"r") as f:
            names["data"+str(counter)] = json.load(f)
            counter+=1

            for i in range(len(names["data"+str(counter)])):
                timestamp.append(names["data"+str(counter)][i]["timestamp"])

with open("timestamp.json","w") as f :
    json.dump(timestamp,f)


# i = 0
# count_list = []
# while i < 34:
#     count = 0
#     for item in data:
#         if (1477260000+i*86400)< int(item["timestamp"]) < (1477260000+(i+1)*86400):
#             count+=1
#     print("count{i} is {num}".format(i = i , num = count))
#     count_list.append(count)
#
#     i+=1
#
#
# # print(count)
# print(count_list)
#
# #draw histogram
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# # plt.hist(count_list,bins = 100,rwidth=0.8)
# plt.bar(range(len(count_list)),count_list)
# # plt.axis([-50,1400,0.5,10000000])
# plt.title("S2-Timestamp-Tx_num")
# plt.xlabel('Timestamp')
# plt.ylabel('Tx num. ')
# # plt.legend()
# # plt.savefig('/Users/fengyangguo/Downloads/S2_In_degree_normalization.png')
# plt.show()
