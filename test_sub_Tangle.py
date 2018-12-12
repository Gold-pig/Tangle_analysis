import matplotlib.pyplot as plt
import networkx as nx

ancestor_list = [5,3,2,1,0]
branch_link = [[0,1],[1,2],[2,3],[3,4],[4,8],[5,9],[6,10],[7,10],[10,11],[9,11],[8,11]]

#method 1
# sub_Tangle = []
# for i in range(len(branch_link)):
#     if branch_link[i][0] in ancestor_list:
#         sub_Tangle.append(branch_link[i])
#
# print(sub_Tangle)

nlink = dict()
for i in ancestor_list:
   nlink[i]=[]

for branch in branch_link:
   if branch[0] in nlink:   # 在 key 中查找
       #nlink[branch[0]] = []
   # if branch[1] not in nlink:
   #     nlink[branch[1]] = []
       nlink[branch[0]].append(branch)
print([nlink])

G = nx.DiGraph()
for i in branch_link :
    a = i[0]
    b = i[1]
    G.add_edge(a,b)


print(G.in_degree[11])
print(list(nx.topological_sort(G)))
print(list(nx.topological_sort(nx.line_graph(G))))

# pos = nx.spring_layout(G)
# nx.draw(G, pos, font_size=16, with_labels=False)
# for p in pos:  # raise text positions
#     pos[p][1] += 0.07
# nx.draw_networkx_labels(G, pos)
# plt.show()

