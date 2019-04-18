import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
name = '6'
with open("/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/tx_per_bucket/MS{}_tx_per_mile_confirm_spe_fast.json".format(name)) as f:
    bucket = json.load(f)
with open("/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/tx_diffsum_divi_indegree_data/MS{}_sum_divide_indegree.json".format(name)) as f:
    diff_cw = json.load(f)

bucket_merge = []
for i in bucket.items():
    i[1].append(int(i[0]))
    bucket_merge.append(i[1])
# print(bucket_merge)


bucket_cw = []
for i in bucket_merge:
    bucket_cw_part = []
    for j in i:
        bucket_cw_part.append(diff_cw['{}'.format(j)])
    bucket_cw.append(bucket_cw_part)

# print(bucket_cw)

bucket_average_cw = []
for i in bucket_cw:
    bucket_average_cw.append(np.mean(i))

print(bucket_average_cw)

chunk_list = [bucket_average_cw[i:i + 100] for i in range(0, len(bucket_average_cw), 100)]
ten_average = []
for i in chunk_list:
    ten_average.append(np.mean(i))

df = pd.read_csv("/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/tx_number_each_bucket/MS{}_per_100mile_data.csv".format(name),usecols=['Mean'])
#    df_x = pd.read_csv("{n}_txs_num_per_bucket.csv".format(n = name),usecols=['Milestone_num'])
#    df_y = pd.read_csv("{n}_txs_num_per_bucket.csv".format(n = name),usecols=['Num of Txs'])


#    Milestone_num = np.array(df_x).tolist()

#    Num_txs = np.array(df_y).tolist()


plt.figure()
plt.scatter(x = 'Mean', y = ten_average, data = df, marker= '.')
plt.xlabel('Amount of transactions')
plt.ylabel('Sum of Difference/indegree')
plt.title('MS{} transaction number and difference of cumulative weight'.format(name))
plt.xscale('log')
plt.yscale('log')
plt.savefig('/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/tx_transactionnumber_cwdiff_plot/MS{}txnumbercwdiff.png'.format(name))









def chunk(l,n):
    chunk_dict_list = []
    chunk_list = [l[i:i + n] for i in range(0, len(l), n)]
