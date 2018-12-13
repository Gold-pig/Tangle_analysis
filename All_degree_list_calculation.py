import matplotlib.pyplot as plt
import networkx as nx
import json
import numpy as np
import math
from collections import Counter
#open all_degree_list

with open("In_degree_list_IRI_1.1.0.json") as f:
    MS1_degree = json.load(f)
with open("In_degree_list_IRI_1.1.2.2_13157.json") as f:
    MS2_degree = json.load(f)
with open("In_degree_list_IRI_1.1.2.4_18675.json") as f:
    MS3_degree = json.load(f)
with open("In_degree_list_IRI_1.1.4.3_61491.json") as f:
    MS4_degree = json.load(f)
with open("In_degree_list_IRI_1.2.4_150354.json") as f:
    MS5_degree = json.load(f)
with open("In_degree_list_IRI_1.3.2.2_216223.json") as f:
    MS6_degree = json.load(f)
with open("In_degree_list_IRI_1.4.0_242662.json") as f:
    MS7_degree = json.load(f)
with open("In_degree_list_IRI_1.4.1.7_337541.json") as f:
    MS8_degree = json.load(f)
with open("In_degree_list_IRI_1.4.2.2_426522.json") as f:
    MS9_degree = json.load(f)
with open("In_degree_list_IRI_1.5.0_587745.json") as f:
    MS10_degree = json.load(f)
with open("In_degree_list_IRI_1.5.3_774804.json") as f:
    MS11_degree = json.load(f)

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    print(result)
    return result
#
# #degree counting
MS1_degree_counting = all_list(MS1_degree)
MS2_degree_counting = all_list(MS2_degree)
MS3_degree_counting = all_list(MS3_degree)
MS4_degree_counting = all_list(MS4_degree)
MS5_degree_counting = all_list(MS5_degree)
MS6_degree_counting = all_list(MS6_degree)
MS7_degree_counting = all_list(MS7_degree)
MS8_degree_counting = all_list(MS8_degree)
MS9_degree_counting = all_list(MS9_degree)
MS10_degree_counting = all_list(MS10_degree)
MS11_degree_counting = all_list(MS11_degree)


# print(S2_degree_counting)
# print(S3_degree_counting)
# print(S4_degree_counting)
# print(S5_degree_counting)
# print(S6_degree_counting)
# print(S7_degree_counting)
# print(S8_degree_counting)
#
# print(S2_degree_counting)
# print(S3_degree_counting)
# print(S4_degree_counting)
# print(S5_degree_counting)
# print(S6_degree_counting)
# print(S7_degree_counting)
# print(S8_degree_counting)
#
# c = Counter(S2_degree_counting) + Counter(S3_degree_counting)+Counter(S4_degree_counting)+Counter(S5_degree_counting)+Counter(S6_degree_counting)+Counter(S7_degree_counting)+Counter(S8_degree_counting)
# c = dict(c)
# print(c)



# with open("degree_list_IRI_1.1.0.json") as f:
#     S2_degree = json.load(f)
# with open("degree_list_IRI_1.1.2.2_13157.json") as f:
#     S3_degree = json.load(f)
# with open("degree_list_IRI_1.1.2.4_18675.json") as f:
#     S4_degree = json.load(f)
# with open("degree_list_IRI_1.1.4.3_61491.json") as f:
#     S5_degree = json.load(f)
# with open("degree_list_IRI_1.2.4_150354.json") as f:
#     S6_degree = json.load(f)
# with open("degree_list_IRI_1.3.2.2_216223.json") as f:
#     S7_degree = json.load(f)
# with open("degree_list_IRI_1.4.0_242662.json") as f:
#     S8_degree = json.load(f)
# #in_degree_counting
# S2_degree_counting = all_list(S2_degree)
# S3_degree_counting = all_list(S3_degree)
# S4_degree_counting = all_list(S4_degree)
# S5_degree_counting = all_list(S5_degree)
# S6_degree_counting = all_list(S6_degree)
# S7_degree_counting = all_list(S7_degree)
# S8_degree_counting = all_list(S8_degree)
#
# print(S2_degree_counting)
# print(S3_degree_counting)
# print(S4_degree_counting)
# print(S5_degree_counting)
# print(S6_degree_counting)
# print(S7_degree_counting)
# print(S8_degree_counting)
