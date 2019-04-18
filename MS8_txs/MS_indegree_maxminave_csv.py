import json
import numpy as np
import pandas as pd


def indegree(name):
    with open("{}_indegree_dict.json".format(name)) as f:
        indegree = json.load(f)

    indegree_list = list(indegree.values())

    print("{}".format(name))
    print("max", max(indegree_list))
    print("min", min(indegree_list))
    print("mean",np.mean(indegree_list))
    print("median", np.median(indegree_list))

    dataframe = pd.DataFrame({'Snapshot':"{}".format(name),'max':max(indegree_list),'min':min(indegree_list),"mean":np.mean(indegree_list),"median":np.median(indegree_list)})
    dataframe.to_csv("{n}_milestone_indegree_percent.csv".format(n = name),index=False,sep=',')

for i in range(1,8):
    indegree("MS{}".format(i))
