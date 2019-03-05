#2019-1-7 10.50am
import matplotlib.pyplot as plt
import json
import os



with open("timestamp_day_num_dict_new.json","r") as f :
    data = json.load(f)


SUM = {}
for i in range(len(data)+1):
    print(sum(data.get(str(j)) for j in range(1,i+1)))
    SUM[i] = (sum(data.get(str(j)) for j in range(1,i+1)))
print(SUM)
print(len(SUM))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# plt.hist(count_list,bins = 100,rwidth=0.8)
plt.bar(range(len(SUM)),SUM.values())
# plt.axis([-50,1400,0.5,10000000])
plt.title("All_Timestamp_Tx_Tendency")
plt.yscale('log')
plt.xlabel('Timestamp')
plt.ylabel('Tx num. ')
# plt.legend()
plt.savefig('/Users/fengyangguo/Downloads/All_Timestamp_tx_tendency.png')
plt.show()




