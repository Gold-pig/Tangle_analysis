#2018-12-04 10.15+1pm doing
import matplotlib.pyplot as plt
import networkx as nx
import json


with open("transactions_2016.json") as f:
    data = json.load(f)

print(int(data[0]["timestamp"]))
print(data[6133])

i = 0
count_list = []
while i < 34:
    count = 0
    for item in data:
        if (1477260000+i*86400)< int(item["timestamp"]) < (1477260000+(i+1)*86400):
            count+=1
    print("count{i} is {num}".format(i = i , num = count))
    count_list.append(count)

    i+=1


# print(count)
print(count_list)

#draw histogram
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# plt.hist(count_list,bins = 100,rwidth=0.8)
plt.bar(range(len(count_list)),count_list)
# plt.axis([-50,1400,0.5,10000000])
plt.title("S2-Timestamp-Tx_num")
plt.xlabel('Timestamp')
plt.ylabel('Tx num. ')
# plt.legend()
# plt.savefig('/Users/fengyangguo/Downloads/S2_In_degree_normalization.png')
plt.show()
