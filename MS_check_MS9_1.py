import json
import networkx as nx



with open("MS9_1.json") as f:
    data = json.load(f)
with open("MS9_milestone_dict.json") as f:
    milestone = json.load(f)
with open("MS9_1_sort_timestamp.json") as f:
    sorted_timestamp = json.load(f)

amount = 0
for i in data:
    if i["address"] == "KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU":
        amount+=1
print(amount)


