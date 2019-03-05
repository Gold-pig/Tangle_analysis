import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import pandas as pd
import math

with open("MS1_diff_amount.json","r") as f:
    diff_amount = json.load(f)
with open("MS1_diff_dict.json","r") as f:
    diff_dict = json.load(f)
with open("transactions_2016.json","r") as f:
    data = json.load(f)


print(diff_dict.get("1"))
