import json
import ijson

# # with open('transactions_2016 with c_weight_correct.json') as f:
with open("IRI_1.4.1.7_337541.json","r") as f:
     data = json.load(f)

# filename = "iri-1.5.5-5.json"
# with open(filename,'rb') as f:


# parser = ijson.parse(open('iri-1.5.5-5.json'))
# i = 0
# for prefix, _, value in parser:
#   print(prefix,value)
#   i +=1
#   if i == 32:
#     break
#
#   if not hash:
#     continue
#   code for processinbg hash



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
    # print(hash_d[item['branch_transaction_hash']])
    trunk_link.append((idx, hash_d[item['trunk_transaction_hash']]))
#
#
# print(branch_link)
# # print(trunk_link )
print(len(data))

with open("branch_link_IRI_1.4.1.7_337541.json") as f:
  f.write(json.dumps(branch_link))
with open("trunk_link_IRI_1.4.1.7_337541.json") as f:
  f.write(json.dumps(trunk_link))

from collections import defaultdict

# 辅助变量
# if
# +1
# 添加索引
#
# 简化 if in  dict方法的
#
# collections库 阅读
