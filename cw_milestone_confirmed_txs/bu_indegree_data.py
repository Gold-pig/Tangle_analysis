import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import seaborn as sns; sns.set()
from scipy.stats import mode

name = "MS1"

with open("{}_tx_per_mile_confirmed.json".format(name)) as f:
    tx_per_mile_confirmed = json.load(f)

with open("{}_tx_per_mile_confirmed_spe.json".format(name)) as f:
    tx_per_mile_confirmed_spec = json.load(f)

with open("/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/MS1_indegree_dict.json".format(name)) as f:
    in_degree_dict = json.load(f)

with open("/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/branch_link_2016.json") as f0:
    branch_link = json.load(f0)

with open("/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/trunk_link_2016.json") as f1:
    trunk_link = json.load(f1)


#build DAG graph
G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

bucket_list = []
bucket_dict = {}

#in_degree statistic
in_degree = []
for i in tx_per_mile_confirmed_spec.items():
    in_degree_d = {}
    in_degree_d["milestone_num"] = i[0]
    in_degree_d["m_in_degree"] = [in_degree_dict[i[0]]]
    n_in_degree = []
    for j in i[1]:
        n_in_degree.append(in_degree_dict["{}".format(j)])
    in_degree_d["n_in_degree"] = n_in_degree
    all_in_degree = [in_degree_dict[i[0]]]+n_in_degree
    # all_in_degree.append([in_degree_dict[i[0]]]+n_in_degree)
    # n_in_degree.append([in_degree_dict[i[0]]])
    in_degree_d["all_in_degree"] = all_in_degree
    in_degree.append(in_degree_d)

print(in_degree)
with open("{}_in_degree_stastic.json".format(name),"w") as f:
    json.dump(in_degree,f)


