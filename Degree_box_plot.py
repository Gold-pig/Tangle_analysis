import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import pandas as pd
import math

with open("degree_list_IRI_1.1.0.json") as f:
    S2_link = json.load(f)
with open("degree_list_IRI_1.1.2.2_13157.json") as f:
    S3_link = json.load(f)
with open("degree_list_IRI_1.1.2.4_18675.json") as f:
    S4_link = json.load(f)
with open("degree_list_IRI_1.1.4.3_61491.json") as f:
    S5_link = json.load(f)
with open("degree_list_IRI_1.2.4_150354.json") as f:
    S6_link = json.load(f)
with open("degree_list_IRI_1.3.2.2_216223.json") as f:
    S7_link = json.load(f)
with open("degree_list_IRI_1.4.0_242662.json") as f:
    S8_link = json.load(f)


plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.sans-serif']=['SimHei']

# df = pd.DataFrame()
#
# df["S2"] = S2_link
# df["S3"] = S3_link
# df["S4"] = S4_link
# df["S5"] = S5_link
# df["S6"] = S6_link
# df["S7"] = S7_link
# df["S8"] = S8_link


s2 = pd.Series(np.array(S2_link))
s3 = pd.Series(np.array(S3_link))
s4 = pd.Series(np.array(S4_link))
s5 = pd.Series(np.array(S5_link))
s6 = pd.Series(np.array(S6_link))
s7 = pd.Series(np.array(S7_link))
s8 = pd.Series(np.array(S8_link))



data = pd.DataFrame({'s2':s2,'s3':s3,'s4':s4,'s4':s5,'s5':s5,'s6':s6,'s7':s7,'s8':s8})
# plt.boxplot(x = df.values, labels= df.columns, whis = 1.5)
plt.title("Degree_boxplt")
plt.xlabel("snapshot")
plt.ylabel("degree_num")
data.boxplot()
plt.show()
