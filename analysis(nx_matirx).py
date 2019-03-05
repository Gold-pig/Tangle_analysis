from networkx import nx
import numpy as np
import json
from operator import __or__
from functools import reduce
import random
from scipy import sparse

cumsum_path = "/tmp/cumsum.txt"

with open('trunk_link_IRI_1.1.2.2_13157.json') as f1:
        trunk_link = json.load(f1)
with open('branch_link_IRI_1.1.2.2_13157.json') as f2:
        branch_link = json.load(f2)

G = nx.DiGraph()

for e in range(len(trunk_link)):
    a = trunk_link[e][0]
    b = trunk_link[e][1]
    G.add_edge(a, b)
for e in range(len(branch_link)):
    a = branch_link[e][0]
    b = branch_link[e][1]
    G.add_edge(a, b)

print("#Nodes: ", len(G.nodes))
print("#Edges: ", len(G.edges))
print("#Indegrees: ", set([G.in_degree(i) for i in G.nodes]))
print("#Outdegrees: ", set([G.out_degree(i) for i in G.nodes]))
print("#Leafs: ", [n for n in G.nodes if G.in_degree(n) == 0])

# Let in the following be G = (V, E) the directed acyclic graph, N = |V| and b the maximal branching factor
N = len(G.nodes)
print("Compute index")
# idxs = [list(G.nodes).index(i) for i in range(N)]

# easy solution: count ancestors for each node, time complexity: O(N^2)
# cumsum = [len(nx.ancestors(G, n)) + 1 for n in G.nodes]

# easy solution, but calculating transitive closure is too memory intense for large graphs
# cumsum = sum(nx.adjacency_matrix(nx.transitive_closure(G)).todense())

print("Compute adjacency matrix")
# better time complexity: O(N * b), but storage complexity: O(N^2)
# A = np.array(nx.adjacency_matrix(G).todense(), dtype=np.uint8)
# nx.adjacency_matrix uses int64, save space by directly using uint8
# A = np.zeros([N, N], dtype=np.uint8)
# for (i, j) in G.edges:
#     A[i, j] = 1
A = nx.adjacency_matrix(G)
A = A.tolil().astype("bool")
print(A)
print("Compute cumulative sum")
for i, n in enumerate(np.flip(list(nx.topological_sort(G)),0)):
    print(i)
    A[n, :] = reduce(__or__, (A[p, :].todense() for p in list(G.successors(n)) + [n]))
    A[n, :] = A[n, :].tolil().astype("bool")
    A[n, n] = 1  # node's own weight
    


cumsum = np.sum(A, dtype=np.uint64, axis=0)

# idea for minor improvement: for each row, make logical-or with predecessors.
# In parallel, add current row to cumsum array, then delete row

print("Testing cumulative sum")

# test procedure (test on all or on a random subset of nodes)
random_selector = lambda: (list(G.nodes)[random.randint(0, N - 1)] for i in range(1000))  # check random subset -> useful for bigger datasets
linear_selector = lambda: (G.nodes)  # check all nodes -> useful for smaller datasets

failed = []
for n in random_selector():
    result = "OK"
    if len(nx.ancestors(G, n)) + 1 != cumsum[n]:
        failed.append({"id": n, "ancestors": len(nx.ancestors(G, n)), "cumulative sum": cumsum[n]})
        result = "FAILED"
    print("Test", n, " -> ", result)

print("Testing done. Failed for", len(failed))

print("Write cumulative sum to", cumsum_path)

np.savetxt(cumsum_path, cumsum)

print("Done.")

