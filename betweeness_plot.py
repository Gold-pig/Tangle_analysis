import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy

with open("beweeness.json") as f:
    data = json.load(f)

with open("In_degree_list_IRI_1.1.0.json") as f0:
    in_degree = json.load(f0)



with open("transactions_2016 with c_weight_correct.json") as f:
    data0 = json.load(f)

value_list = data.values()

# print(value_list)
#
# print(max(value_list))
#
# def get_keys(d, value):
#     return [k for k,v in d.items() if v == value]
#
# print(get_keys(data,0.03851916250156887))
# print(in_degree[3263])
# print(data0[3263])

i = 0
count_list = []
count_zero = 0
for item in value_list:
    if item == 0:
        count_zero+=1
print(count_zero)

while i < 10:
    count = 0
    for item in value_list:
        if (i*0.004)< item < ((i+1)*0.004):
            count+=1
    print("count{i} is {num}".format(i = i , num = count))
    count_list.append(count)

    i+=1

print(count_list)
print(sum(count_list))
all  = [count_zero] + count_list
print(all)

#draw bar

x = numpy.arange(0,0.0404,0.004)
x_axis = list(x)
# print(x_axis)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# plt.hist(count_list,bins = 100,rwidth=0.8)
plt.bar( range(0,11),all)
plt.xticks(range(0,11),x_axis)
plt.yscale('log')
# plt.axis([0,0.04,0,22000])
plt.title("S2-Betweeness-Tx_num")
plt.xlabel('Betweeness')
plt.ylabel('Tx num. ')
# plt.legend()
# plt.savefig('/Users/fengyangguo/Downloads/S2_In_degree_normalization.png')
plt.show()
