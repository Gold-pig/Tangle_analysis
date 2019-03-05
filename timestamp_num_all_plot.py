#2019-1-7 10.25ampm
import matplotlib.pyplot as plt
import json
import os



with open("timestamp_day_num_dict.json","r") as f :
    data = json.load(f)


# print(data.values())
# # print(count)
# print(count_list)
#
# #draw histogram
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# plt.hist(count_list,bins = 100,rwidth=0.8)
plt.bar(range(len(data)),data.values())
# plt.axis([-50,1400,0.5,10000000])
plt.title("All_Timestamp-Tx_num")
plt.yscale('log')
plt.xlabel('Days')
plt.ylabel('Tx num. ')
# plt.legend()
plt.savefig('/Users/fengyangguo/Downloads/All_Timestamp-Tx_num.png')
plt.show()
