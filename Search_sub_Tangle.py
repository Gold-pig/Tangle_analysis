import matplotlib.pyplot as plt
import networkx as nx
import json


#open the .json database file
with open("transactions_2016 with c_weight_correct.json") as f:
    data = json.load(f)


#hashmap function to get the branch_link and trunk link
hash_d = dict()
branch_d = dict()
trunk_d = dict()
branch_link = []
trunk_link = []
idata = []
for idx, item in enumerate(data):
  hash_d[item['hash']] = idx
  branch_d[item['trunk_transaction_hash']] = idx
  trunk_d[item['branch_transaction_hash']] = idx
  idata.append(item)

for idx, item in enumerate(idata):
  if item['branch_transaction_hash'] in hash_d:
    branch_link.append((idx, hash_d[item['branch_transaction_hash']]))
  if item['trunk_transaction_hash'] in hash_d:
    trunk_link.append((idx, hash_d[item['trunk_transaction_hash']]))

print(branch_link)
print(trunk_link)


print(data[11]['hash'],data[11]['branch_transaction_hash'],data[11]['trunk_transaction_hash'])
print(data[43597]['hash'],data[43597]['branch_transaction_hash'],data[43597]['trunk_transaction_hash'])



#convert the list to json then store in .json
def store():
    with open('trunk_link_2016.json', 'w') as f0:
        f0.write(json.dumps(trunk_link))
    with open('branch_link_2016.json', 'w') as f1:
        f1.write(json.dumps(branch_link))
store()

