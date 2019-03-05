import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import math
import datashader as ds
from colorcet import fire
from datashader import transfer_functions as tf
import bokeh.plotting as bp
import seaborn as sns; sns.set()



df = pd.read_csv('transactions_2016_topology_time.csv',usecols=['Attach_order', 'Timestamp'])
df.tail()
print(df.tail())


sns.jointplot(x='Attach_order', y='Timestamp', data=df)
# plt.title("Attachment")
plt.show()


# agg = ds.Canvas().points(df, 'Timestamp', 'cumulative_weight')
# img = tf.set_background(tf.shade(agg, cmap=fire),"black")
