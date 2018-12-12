import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import math
#open link file

def all_degree_list():
    with open("branch_link_IRI_1.5.3_774804.json") as f0:
        branch_link = json.load(f0)

    with open("trunk_link_IRI_1.5.3_774804.json") as f1:
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

    #construct degree list and store in .json
    #construct in_degree list and store in .json
    #construct out_degree list and store in .json

    degree_list = []
    in_degree_list = []
    out_degree_list = []
    for i in range(0,2241876):
        degree_list.append(G.degree(i))
        in_degree_list.append(G.in_degree(i))
        out_degree_list.append(G.out_degree(i))


    print("max degree", max(degree_list))
    print("max in_degree:",max(in_degree_list))
    print("max out_degree", max(out_degree_list))

    with open('degree_list_IRI_1.5.3_774804.json', 'w') as f:
            f.write(json.dumps(degree_list))
    with open('In_degree_list_IRI_1.5.3_774804.json', 'w') as f:
            f.write(json.dumps(in_degree_list))
    with open('Out_degree_list_IRI_1.5.3_774804.json', 'w') as f:
            f.write(json.dumps(out_degree_list))

    return

all_degree_list()






