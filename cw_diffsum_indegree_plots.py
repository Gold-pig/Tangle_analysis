import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import math
from scipy.stats import mode


name = "MS1"

with open("{}_predecessor.json".format(name),"r") as f:
    predecessor = json.load(f)

with open("{}_sum_divide_indegree.json".format(name),"r") as f:
    sum_divide_indegree = json.load(f)

print(sum_divide_indegree)




#histogram
sum_divide_indegree_list = []
for i in sum_divide_indegree.items():
    sum_divide_indegree_list.append(i[1])
print(sum_divide_indegree_list)

# #Statistic for amount of txs confirmed per milestone
print('{n}_sum_divide_indegree'.format(n = name))
print("max",max(list(sum_divide_indegree_list)))
print("min",min(list(sum_divide_indegree_list)))
print("mean",np.mean(sum_divide_indegree_list))     #pingjun
print("median",np.median(list(sum_divide_indegree_list))) #zhongwei
print("mode",mode(list(sum_divide_indegree_list))) #zhongshu
print("number of sites",len(sum_divide_indegree_list))


plt.figure()
plt.hist(sum_divide_indegree_list, bins=100)
plt.xlabel("Sum of Difference/In-degree")
plt.ylabel("Amount of Sites")
plt.title("{}_Sum of Difference/In-degree".format(name))
plt.yscale("log")
plt.show()
plt.savefig("{}_sum_divide_indegree.png".format(name))

