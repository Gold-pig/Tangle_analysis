#2018-12-04 10.15+1pm doing
import matplotlib.pyplot as plt
import networkx as nx
import json


with open("IRI_1.5.3_774804.json") as f:
    data = json.load(f)

#print(int(data[0]["timestamp"]))
#print(data[6133])

i = -5
count_list = []
while i <90:
    count = 0
    for item in data:
        if (1531087200+i*86400)< int(item["timestamp"]) < (1531087200+(i+1)*86400):
            count+=1
    print("count{i} is {num}".format(i = i , num = count))
    count_list.append(count)

    i+=1


#!!!find the tx out of snapshot period!!!!
over_list = []
for item in data:
    if int(item["timestamp"]) <=1531087200 or int(item["timestamp"]) >= (1531087200+(101)*86400)  :
        over_list.append(item["hash"])
    elif int(item["timestamp"]) == " ":
        print("null")
print("overlist",over_list)
print(len(over_list))
with open("overlist_timestamp.json","w") as f:
    json.dump(over_list,f)

SUM = []
for i in range(len(count_list)):
    SUM.append(sum(count_list[0:(i+1)]))
print(SUM)
    

#draw histogram
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# plt.hist(count_list,bins = 100,rwidth=0.8)
plt.bar(range(len(SUM)),SUM)
# plt.axis([-50,1400,0.5,10000000])
plt.title("MS11_Timestamp_Tx_Tendency")
plt.xlabel('Timestamp')
plt.ylabel('Tx num. ')
# plt.legend()
#plt.savefig('MS10_Timestamp_tx_tendency.png')
plt.show()
