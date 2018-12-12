import matplotlib.pyplot as plt

import networkx as nx
import json
import numpy as np
import math

#degree dict
# sum ?degree_dict = {1: 9, 2: 82116, 3: 4763050, 4: 2554460, 5: 1248128, 6: 506719, 7: 208594, 8: 100283, 9: 56675, 10: 33920, 11: 22336, 12: 15052, 13: 10621, 14: 7463, 15: 5686, 16: 4033, 17: 3138, 18: 2402, 19: 1908, 20: 1616, 21: 1245, 22: 1077, 23: 847, 24: 683, 25: 566, 26: 520, 27: 423, 28: 348, 29: 349, 30: 264, 31: 245, 32: 199, 33: 174, 34: 146, 35: 141, 36: 94, 38: 100, 39: 88, 41: 75, 45: 52, 51: 22, 54: 27, 55: 24, 110: 1, 40: 78, 42: 78, 43: 51, 44: 49, 57: 14, 62: 16, 74: 10, 75: 9, 85: 7, 37: 101, 46: 43, 47: 33, 48: 32, 49: 25, 50: 23, 52: 21, 53: 19, 56: 18, 58: 14, 59: 14, 60: 18, 61: 12, 63: 18, 64: 16, 66: 14, 67: 14, 69: 7, 70: 8, 71: 11, 72: 7, 76: 8, 78: 12, 80: 7, 82: 6, 86: 7, 88: 8, 89: 4, 90: 5, 92: 3, 93: 7, 95: 5, 96: 5, 97: 7, 99: 4, 100: 2, 101: 3, 102: 9, 104: 4, 105: 6, 106: 8, 108: 2, 114: 3, 122: 2, 128: 2, 138: 2, 140: 2, 143: 1, 144: 1, 146: 3, 149: 2, 195: 2, 68: 10, 73: 6, 77: 10, 83: 5, 84: 5, 87: 1, 91: 3, 94: 3, 111: 3, 112: 3, 115: 2, 118: 4, 119: 2, 120: 1, 123: 1, 124: 3, 127: 2, 129: 2, 130: 3, 135: 1, 136: 1, 147: 1, 152: 1, 158: 1, 161: 2, 167: 1, 173: 1, 188: 1, 190: 1, 194: 1, 203: 1, 204: 2, 206: 4, 517: 1, 217: 1, 226: 1, 230: 1, 232: 2, 246: 1, 253: 1, 258: 1, 265: 1, 294: 1, 305: 1, 340: 1, 398: 1, 506: 1, 65: 6, 79: 6, 81: 4, 1119: 1, 126: 2, 139: 1, 169: 1, 179: 1, 193: 1, 214: 1, 282: 1, 98: 2, 615: 1, 107: 5, 113: 2, 125: 2, 131: 1, 133: 2, 145: 1, 157: 1, 164: 1, 165: 1, 174: 1, 175: 1, 177: 1, 178: 1, 201: 1, 243: 1, 251: 1, 272: 1, 283: 1, 300: 1, 325: 1, 327: 1, 400: 1, 498: 1, 137: 1, 181: 1, 196: 1, 1364: 1, 1012: 1}
# degree_dict = {1: 1, 2: 3378, 3: 19606, 4: 13405, 5: 4096, 6: 1279, 7: 526, 8: 325, 9: 195, 10: 138, 11: 111, 12: 105, 13: 71, 14: 57, 15: 63, 16: 44, 17: 29, 18: 27, 19: 28, 20: 21, 21: 10, 22: 18, 23: 8, 24: 5, 25: 5, 26: 9, 27: 3, 28: 4, 29: 3, 30: 3, 31: 4, 32: 1, 33: 2, 34: 1, 35: 3, 36: 3, 38: 3, 39: 2, 41: 1, 45: 1, 51: 1, 54: 1, 55: 1, 110: 1}
# degree_dict = {1: 3, 2: 1201, 3: 51976, 4: 34309, 5: 16853, 6: 6521, 7: 2431, 8: 885, 9: 362, 10: 191, 11: 123, 12: 77, 13: 73, 14: 65, 15: 48, 16: 37, 17: 29, 18: 22, 19: 22, 20: 26, 21: 15, 22: 10, 23: 10, 24: 8, 25: 8, 26: 5, 27: 2, 28: 8, 29: 3, 30: 2, 31: 4, 32: 3, 33: 6, 34: 3, 35: 2, 36: 2, 38: 2, 40: 1, 41: 1, 42: 1, 43: 1, 44: 2, 45: 2, 51: 1, 54: 1, 55: 1, 57: 2, 62: 1, 74: 1, 75: 1, 85: 1}
# degree_dict = {1: 1, 2: 1236, 3: 43776, 4: 24968, 5: 11340, 6: 4632, 7: 1702, 8: 658, 9: 250, 10: 135, 11: 70, 12: 53, 13: 36, 14: 26, 15: 15, 16: 21, 17: 13, 18: 14, 19: 11, 20: 10, 21: 10, 22: 9, 23: 15, 24: 2, 25: 5, 26: 5, 27: 4, 28: 2, 29: 3, 30: 3, 31: 7, 32: 5, 33: 3, 34: 3, 35: 1, 36: 1, 37: 3, 38: 4, 39: 3, 40: 2, 41: 3, 42: 3, 43: 1, 44: 3, 45: 2, 46: 3, 47: 2, 48: 2, 49: 4, 50: 2, 51: 4, 52: 2, 53: 2, 54: 2, 55: 1, 56: 5, 58: 1, 59: 3, 60: 2, 61: 2, 62: 2, 63: 5, 64: 4, 66: 1, 67: 3, 69: 1, 70: 2, 71: 2, 72: 1, 74: 4, 75: 1, 76: 2, 78: 3, 80: 1, 82: 1, 85: 1, 86: 2, 88: 1, 89: 1, 90: 1, 92: 2, 93: 2, 95: 2, 96: 1, 97: 2, 99: 1, 100: 1, 101: 1, 102: 2, 104: 1, 105: 1, 106: 3, 108: 1, 114: 1, 122: 1, 128: 1, 138: 1, 140: 1, 143: 1, 144: 1, 146: 1, 149: 1, 195: 1}
# degree_dict = {1: 1, 2: 70128, 3: 1139455, 4: 686003, 5: 355919, 6: 146883, 7: 53572, 8: 19562, 9: 8821, 10: 4455, 11: 2669, 12: 1807, 13: 1095, 14: 734, 15: 528, 16: 337, 17: 251, 18: 213, 19: 190, 20: 147, 21: 121, 22: 104, 23: 106, 24: 105, 25: 93, 26: 78, 27: 81, 28: 76, 29: 104, 30: 57, 31: 57, 32: 44, 33: 41, 34: 47, 35: 49, 36: 25, 37: 36, 38: 33, 39: 31, 40: 39, 41: 29, 42: 31, 43: 14, 44: 23, 45: 24, 46: 17, 47: 14, 48: 16, 49: 16, 50: 9, 51: 6, 52: 10, 53: 6, 54: 12, 55: 6, 56: 6, 57: 3, 58: 3, 59: 3, 60: 6, 61: 3, 62: 8, 63: 5, 64: 4, 66: 3, 67: 1, 68: 1, 69: 2, 70: 4, 71: 3, 72: 2, 73: 2, 74: 2, 75: 1, 77: 4, 78: 1, 80: 2, 82: 1, 83: 2, 84: 2, 85: 2, 86: 2, 87: 1, 88: 1, 91: 1, 93: 1, 94: 1, 96: 2, 97: 3, 99: 1, 101: 1, 102: 2, 104: 1, 106: 2, 108: 1, 111: 2, 112: 2, 115: 1, 118: 4, 119: 2, 120: 1, 122: 1, 123: 1, 124: 1, 127: 1, 128: 1, 129: 1, 130: 2, 135: 1, 136: 1, 138: 1, 140: 1, 146: 1, 147: 1, 149: 1, 152: 1, 158: 1, 161: 1, 167: 1, 173: 1, 188: 1, 190: 1, 194: 1, 203: 1, 204: 2, 206: 3, 517: 1, 217: 1, 226: 1, 230: 1, 232: 1, 246: 1, 253: 1, 258: 1, 265: 1, 294: 1, 305: 1, 340: 1, 398: 1, 506: 1}
# degree_dict = {1: 1, 2: 605, 3: 1613192, 4: 1033237, 5: 529042, 6: 207158, 7: 75143, 8: 30014, 9: 14484, 10: 7452, 11: 4725, 12: 3104, 13: 2168, 14: 1558, 15: 1322, 16: 925, 17: 803, 18: 633, 19: 483, 20: 402, 21: 328, 22: 290, 23: 215, 24: 175, 25: 137, 26: 141, 27: 123, 28: 95, 29: 97, 30: 77, 31: 63, 32: 42, 33: 41, 34: 34, 35: 26, 36: 26, 37: 27, 38: 25, 39: 24, 40: 16, 41: 19, 42: 20, 43: 13, 44: 6, 45: 10, 46: 7, 47: 9, 48: 7, 49: 2, 50: 5, 51: 3, 52: 5, 53: 5, 54: 6, 55: 4, 56: 2, 57: 3, 58: 2, 59: 1, 60: 4, 61: 2, 62: 1, 63: 4, 64: 1, 65: 2, 66: 5, 67: 2, 68: 4, 69: 1, 71: 1, 72: 1, 73: 1, 74: 1, 78: 1, 79: 2, 80: 2, 81: 2, 82: 1, 86: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 1119: 1, 96: 1, 95: 1, 100: 1, 102: 1, 104: 1, 126: 1, 127: 1, 139: 1, 146: 1, 169: 1, 179: 1, 193: 1, 214: 1, 282: 1}
# degree_dict = {1: 1, 2: 4917, 3: 1250934, 4: 441518, 5: 176424, 6: 76838, 7: 45723, 8: 31872, 9: 21812, 10: 14905, 11: 10614, 12: 7409, 13: 5525, 14: 3936, 15: 2969, 16: 2199, 17: 1701, 18: 1300, 19: 1024, 20: 920, 21: 684, 22: 589, 23: 431, 24: 355, 25: 293, 26: 258, 27: 190, 28: 145, 29: 130, 30: 110, 31: 101, 32: 93, 33: 69, 34: 55, 35: 54, 36: 33, 37: 33, 38: 29, 39: 24, 40: 17, 41: 20, 42: 20, 43: 16, 44: 13, 45: 13, 46: 13, 47: 7, 48: 5, 49: 3, 50: 6, 51: 6, 52: 4, 53: 4, 54: 5, 55: 9, 56: 3, 57: 5, 58: 5, 59: 7, 60: 5, 61: 4, 62: 4, 63: 4, 64: 6, 65: 4, 66: 3, 67: 6, 68: 5, 69: 3, 70: 2, 71: 5, 72: 3, 73: 2, 75: 5, 76: 5, 77: 6, 78: 6, 79: 3, 80: 2, 81: 2, 82: 3, 83: 3, 84: 3, 85: 3, 86: 1, 88: 5, 89: 1, 90: 3, 91: 1, 93: 3, 95: 2, 96: 1, 97: 2, 98: 2, 99: 1, 101: 1, 102: 3, 615: 1, 105: 5, 106: 3, 107: 3, 111: 1, 112: 1, 113: 2, 114: 2, 115: 1, 124: 2, 125: 2, 126: 1, 129: 1, 130: 1, 131: 1, 133: 2, 145: 1, 157: 1, 164: 1, 165: 1, 174: 1, 175: 1, 177: 1, 178: 1, 195: 1, 201: 1, 232: 1, 243: 1, 251: 1, 272: 1, 283: 1, 300: 1, 325: 1, 327: 1, 400: 1, 498: 1}
# degree_dict = {1: 1, 2: 651, 3: 644111, 4: 321020, 5: 154454, 6: 63408, 7: 29497, 8: 16967, 9: 10751, 10: 6644, 11: 4024, 12: 2497, 13: 1653, 14: 1087, 15: 741, 16: 470, 17: 312, 18: 193, 19: 150, 20: 90, 21: 77, 22: 57, 23: 62, 24: 33, 25: 25, 26: 24, 27: 20, 28: 18, 29: 9, 30: 12, 31: 9, 32: 11, 33: 12, 34: 3, 35: 6, 36: 4, 37: 2, 38: 4, 39: 4, 40: 3, 41: 2, 42: 3, 43: 6, 44: 2, 161: 1, 46: 3, 47: 1, 48: 2, 137: 1, 51: 1, 50: 1, 53: 2, 181: 1, 55: 2, 56: 2, 57: 1, 58: 3, 60: 1, 61: 1, 64: 1, 66: 2, 67: 2, 196: 1, 73: 1, 74: 2, 75: 1, 76: 1, 206: 1, 79: 1, 78: 1, 1364: 1, 86: 1, 89: 1, 94: 1, 99: 1, 102: 1, 104: 1, 107: 2, 1012: 1}

#in degree dict
# sum ? degree_dict = {1: 4826614, 2: 2567934, 3: 1251485, 4: 507785, 5: 208893, 6: 100475, 7: 56756, 8: 33955, 9: 22364, 10: 15058, 11: 10628, 12: 7463, 13: 5693, 14: 4035, 15: 3136, 16: 2399, 17: 1913, 18: 1615, 19: 1245, 20: 1078, 21: 847, 22: 683, 23: 566, 24: 518, 25: 425, 26: 348, 27: 347, 28: 266, 29: 244, 30: 200, 31: 174, 32: 146, 33: 141, 34: 94, 36: 100, 37: 88, 39: 76, 43: 52, 49: 22, 52: 27, 53: 24, 108: 1, 38: 77, 40: 78, 41: 51, 42: 49, 55: 14, 60: 16, 72: 10, 73: 9, 83: 7, 35: 101, 44: 43, 45: 33, 46: 32, 47: 25, 48: 23, 50: 21, 51: 19, 54: 18, 56: 14, 57: 14, 58: 18, 59: 12, 61: 18, 62: 16, 64: 14, 65: 14, 67: 7, 68: 8, 69: 11, 70: 7, 74: 8, 76: 12, 78: 7, 80: 6, 84: 7, 86: 8, 87: 4, 88: 5, 90: 3, 91: 7, 93: 5, 94: 5, 95: 7, 97: 4, 98: 2, 99: 3, 100: 9, 102: 4, 103: 6, 104: 8, 106: 2, 112: 3, 120: 2, 126: 2, 136: 2, 138: 2, 141: 1, 142: 1, 144: 3, 147: 2, 193: 2, 66: 10, 71: 6, 75: 10, 81: 5, 82: 5, 85: 1, 89: 3, 92: 3, 109: 3, 110: 3, 113: 2, 116: 4, 117: 2, 118: 1, 121: 1, 122: 3, 125: 2, 127: 2, 128: 3, 133: 1, 134: 1, 145: 1, 150: 1, 156: 1, 159: 2, 515: 1, 165: 1, 171: 1, 186: 1, 188: 1, 192: 1, 201: 1, 202: 2, 204: 4, 215: 1, 224: 1, 228: 1, 230: 2, 244: 1, 251: 1, 256: 1, 263: 1, 292: 1, 303: 1, 338: 1, 396: 1, 504: 1, 63: 6, 77: 6, 79: 4, 1117: 1, 124: 2, 137: 1, 167: 1, 177: 1, 191: 1, 212: 1, 280: 1, 96: 2, 613: 1, 105: 5, 111: 2, 123: 2, 129: 1, 131: 2, 143: 1, 155: 1, 162: 1, 163: 1, 172: 1, 173: 1, 175: 1, 176: 1, 199: 1, 241: 1, 249: 1, 270: 1, 281: 1, 298: 1, 323: 1, 325: 1, 398: 1, 496: 1, 135: 1, 179: 1, 194: 1, 1362: 1, 1010: 1}
# degree_dict = {0: 1, 1: 22833, 2: 13504, 3: 4136, 4: 1291, 5: 526, 6: 325, 7: 195, 8: 138, 9: 111, 10: 105, 11: 71, 12: 57, 13: 63, 14: 44, 15: 29, 16: 27, 17: 28, 18: 21, 19: 10, 20: 18, 21: 8, 22: 5, 23: 5, 24: 9, 25: 3, 26: 4, 27: 3, 28: 3, 29: 4, 30: 1, 31: 2, 32: 1, 33: 3, 34: 3, 36: 3, 37: 2, 39: 1, 43: 1, 49: 1, 52: 1, 53: 1, 108: 1}
# degree_dict = {0: 1, 1: 53101, 2: 34379, 3: 16859, 4: 6522, 5: 2432, 6: 884, 7: 363, 8: 191, 9: 123, 10: 77, 11: 73, 12: 65, 13: 48, 14: 37, 15: 29, 16: 22, 17: 22, 18: 26, 19: 15, 20: 10, 21: 10, 22: 8, 23: 8, 24: 5, 25: 2, 26: 8, 27: 3, 28: 2, 29: 4, 30: 3, 31: 6, 32: 3, 33: 2, 34: 2, 36: 2, 38: 1, 39: 1, 40: 1, 41: 1, 42: 2, 43: 2, 49: 1, 52: 1, 53: 1, 55: 2, 60: 1, 72: 1, 73: 1, 83: 1}
# degree_dict = {0: 1, 1: 44866, 2: 25086, 3: 11355, 4: 4643, 5: 1701, 6: 661, 7: 249, 8: 136, 9: 70, 10: 53, 11: 36, 12: 26, 13: 15, 14: 21, 15: 13, 16: 13, 17: 12, 18: 10, 19: 10, 20: 9, 21: 15, 22: 2, 23: 5, 24: 5, 25: 4, 26: 2, 27: 3, 28: 3, 29: 7, 30: 5, 31: 3, 32: 3, 33: 1, 34: 1, 35: 3, 36: 4, 37: 3, 38: 2, 39: 3, 40: 3, 41: 1, 42: 3, 43: 2, 44: 3, 45: 2, 46: 2, 47: 4, 48: 2, 49: 4, 50: 2, 51: 2, 52: 2, 53: 1, 54: 5, 56: 1, 57: 3, 58: 2, 59: 2, 60: 2, 61: 5, 62: 4, 64: 1, 65: 3, 67: 1, 68: 2, 69: 2, 70: 1, 72: 4, 73: 1, 74: 2, 76: 3, 78: 1, 80: 1, 83: 1, 84: 2, 86: 1, 87: 1, 88: 1, 90: 2, 91: 2, 93: 2, 94: 1, 95: 2, 97: 1, 98: 1, 99: 1, 100: 2, 102: 1, 103: 1, 104: 3, 106: 1, 112: 1, 120: 1, 126: 1, 136: 1, 138: 1, 141: 1, 142: 1, 144: 1, 147: 1, 193: 1}
# degree_dict = {0: 1, 1: 1192126, 2: 698767, 3: 359033, 4: 147875, 5: 53848, 6: 19730, 7: 8899, 8: 4482, 9: 2691, 10: 1810, 11: 1102, 12: 734, 13: 534, 14: 337, 15: 249, 16: 212, 17: 193, 18: 147, 19: 120, 20: 105, 21: 106, 22: 105, 23: 93, 24: 76, 25: 83, 26: 76, 27: 102, 28: 59, 29: 57, 30: 44, 31: 41, 32: 47, 33: 49, 34: 25, 35: 36, 36: 33, 37: 31, 38: 38, 39: 30, 40: 31, 41: 14, 42: 23, 43: 24, 44: 17, 45: 14, 46: 16, 47: 16, 48: 9, 49: 6, 50: 10, 51: 6, 52: 12, 53: 6, 54: 6, 55: 3, 56: 3, 57: 3, 58: 6, 59: 3, 60: 8, 61: 5, 62: 4, 64: 3, 65: 1, 66: 1, 67: 2, 68: 4, 69: 3, 70: 2, 71: 2, 72: 2, 73: 1, 75: 4, 76: 1, 78: 2, 80: 1, 81: 2, 82: 2, 83: 2, 84: 2, 85: 1, 86: 1, 89: 1, 91: 1, 92: 1, 94: 2, 95: 3, 97: 1, 99: 1, 100: 2, 102: 1, 104: 2, 106: 1, 109: 2, 110: 2, 113: 1, 116: 4, 117: 2, 118: 1, 120: 1, 121: 1, 122: 1, 125: 1, 126: 1, 127: 1, 128: 2, 133: 1, 134: 1, 136: 1, 138: 1, 144: 1, 145: 1, 147: 1, 150: 1, 156: 1, 159: 1, 515: 1, 165: 1, 171: 1, 186: 1, 188: 1, 192: 1, 201: 1, 202: 2, 204: 3, 215: 1, 224: 1, 228: 1, 230: 1, 244: 1, 251: 1, 256: 1, 263: 1, 292: 1, 303: 1, 338: 1, 396: 1, 504: 1}
# degree_dict = {0: 1, 1: 1613780, 2: 1033247, 3: 529045, 4: 207161, 5: 75143, 6: 30014, 7: 14485, 8: 7452, 9: 4725, 10: 3104, 11: 2168, 12: 1558, 13: 1322, 14: 925, 15: 803, 16: 633, 17: 483, 18: 402, 19: 328, 20: 290, 21: 215, 22: 175, 23: 137, 24: 141, 25: 123, 26: 95, 27: 97, 28: 77, 29: 63, 30: 42, 31: 41, 32: 34, 33: 26, 34: 26, 35: 27, 36: 25, 37: 24, 38: 16, 39: 19, 40: 20, 41: 13, 42: 6, 43: 10, 44: 7, 45: 9, 46: 7, 47: 2, 48: 5, 49: 3, 50: 5, 51: 5, 52: 6, 53: 4, 54: 2, 55: 3, 56: 2, 57: 1, 58: 4, 59: 2, 60: 1, 61: 4, 62: 1, 63: 2, 64: 5, 65: 2, 66: 4, 67: 1, 69: 1, 70: 1, 71: 1, 72: 1, 76: 1, 77: 2, 78: 2, 79: 2, 80: 1, 84: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 1117: 1, 94: 1, 93: 1, 98: 1, 100: 1, 102: 1, 124: 1, 125: 1, 137: 1, 144: 1, 167: 1, 177: 1, 191: 1, 212: 1, 280: 1}
# degree_dict = {0: 1, 1: 1255163, 2: 441918, 3: 176600, 4: 76885, 5: 45745, 6: 31894, 7: 21814, 8: 14912, 9: 10620, 10: 7412, 11: 5525, 12: 3936, 13: 2970, 14: 2201, 15: 1701, 16: 1299, 17: 1025, 18: 919, 19: 685, 20: 589, 21: 431, 22: 355, 23: 293, 24: 258, 25: 190, 26: 145, 27: 130, 28: 110, 29: 100, 30: 94, 31: 69, 32: 55, 33: 54, 34: 33, 35: 33, 36: 29, 37: 24, 38: 17, 39: 20, 40: 20, 41: 16, 42: 13, 43: 13, 44: 13, 45: 7, 46: 5, 47: 3, 48: 6, 49: 6, 50: 4, 51: 4, 52: 5, 53: 9, 54: 3, 55: 5, 56: 5, 57: 7, 58: 5, 59: 4, 60: 4, 61: 4, 62: 6, 63: 4, 64: 3, 65: 6, 66: 5, 67: 3, 68: 2, 69: 5, 70: 3, 71: 2, 73: 5, 74: 5, 75: 6, 76: 6, 77: 3, 78: 2, 79: 2, 80: 3, 81: 3, 82: 3, 83: 3, 84: 1, 86: 5, 87: 1, 88: 3, 89: 1, 91: 3, 93: 2, 94: 1, 95: 2, 96: 2, 97: 1, 99: 1, 100: 3, 613: 1, 103: 5, 104: 3, 105: 3, 109: 1, 110: 1, 111: 2, 112: 2, 113: 1, 122: 2, 123: 2, 124: 1, 127: 1, 128: 1, 129: 1, 131: 2, 143: 1, 155: 1, 162: 1, 163: 1, 172: 1, 173: 1, 175: 1, 176: 1, 193: 1, 199: 1, 230: 1, 241: 1, 249: 1, 270: 1, 281: 1, 298: 1, 323: 1, 325: 1, 398: 1, 496: 1}
# degree_dict = {0: 1, 1: 644745, 2: 321033, 3: 154457, 4: 63408, 5: 29498, 6: 16967, 7: 10751, 8: 6644, 9: 4024, 10: 2497, 11: 1653, 12: 1087, 13: 741, 14: 470, 15: 312, 16: 193, 17: 150, 18: 90, 19: 77, 20: 57, 21: 62, 22: 33, 23: 25, 24: 24, 25: 20, 26: 18, 27: 9, 28: 12, 29: 9, 30: 11, 31: 12, 32: 3, 33: 6, 34: 4, 35: 2, 36: 4, 37: 4, 38: 3, 39: 2, 40: 3, 41: 6, 42: 2, 159: 1, 44: 3, 45: 1, 46: 2, 135: 1, 48: 1, 49: 1, 51: 2, 179: 1, 53: 2, 54: 2, 55: 1, 56: 3, 58: 1, 59: 1, 62: 1, 64: 2, 65: 2, 194: 1, 71: 1, 72: 2, 73: 1, 74: 1, 204: 1, 77: 1, 76: 1, 1362: 1, 84: 1, 87: 1, 92: 1, 97: 1, 100: 1, 102: 1, 105: 2, 1010: 1}


# degree_num = list(degree_dict.keys())
# degree_cout = list(degree_dict.values())
#
#
# fig = plt.figure()
# # ax1 = fig.add_subplot(121)
# # plt.pie(y,labels = x,autopct= '%1.2f%%' )
# plt.title("S2")
# plt.xlabel('In_degree num.')
# plt.ylabel('nodes num. ')
# #dram histogram
# # log_list = []
# # for i in list(in_degree_statistic.values()):
# #     log_list.append(math.log(i))
#
# # print(log_list)
# # ax2 = fig.add_subplot(122)
# # plt.bar(in_degree_statistic.keys(),log_list, fc = 'b')
# # plt.show()
#
# #degree distribution
# # print(nx.degree_histogram(G))
# # degree =  nx.degree_histogram(G)          #返回图中所有节点的度分布序列
# x = degree_num                             #生成x轴序列，从1到最大度
# # y = degree_cout
# y = [z / float(sum(degree_cout)) for z in degree_cout]
# #将频次转换为频率，这用到Python的一个小技巧：列表内涵，Python的确很方便：）
# # ax3 = fig.add_subplot(122)
#
# plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线
#
#
# plt.show()                                                            #显示图表


#histogram for degree
# with open("degree_list_IRI_1.1.0.json") as f:
#      data2 = json.load(f)
# with open("degree_list_IRI_1.1.2.2_13157.json") as f:
#       data3 = json.load(f)
# with open("degree_list_IRI_1.1.2.4_18675.json") as f:
#       data4 = json.load(f)
# with open("degree_list_IRI_1.1.4.3_61491.json") as f:
#       data5 = json.load(f)
# with open("degree_list_IRI_1.2.4_150354.json") as f:
#       data6 = json.load(f)
# with open("degree_list_IRI_1.3.2.2_216223.json") as f:
#      data7 = json.load(f)
# with open("degree_list_IRI_1.4.0_242662.json") as f:
#      data8 = json.load(f)
# # bins = [0,10,20,30,40,50,60,70,80,90,100,110]
# data = data2+data3+data4+data5+data6+data7+data8
#
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
#
# ax.set_yscale('log')
#
# plt.hist(data,bins = 100,rwidth=0.8)
# plt.title("All_degree")
# plt.xlabel('Degree num.')
# plt.ylabel('nodes num. ')
# plt.savefig('/Users/fengyangguo/Downloads/All_degree.png')
# plt.show()


#histogram for in-degree
# with open("In_degree_list_IRI_1.1.0.json") as f:
#      data2 = json.load(f)
# with open("In_degree_list_IRI_1.1.2.2_13157.json") as f:
#       data3 = json.load(f)
# with open("In_degree_list_IRI_1.1.2.4_18675.json") as f:
#       data4 = json.load(f)
# with open("In_degree_list_IRI_1.1.4.3_61491.json") as f:
#       data5 = json.load(f)
# with open("In_degree_list_IRI_1.2.4_150354.json") as f:
#       data6 = json.load(f)
# with open("In_degree_list_IRI_1.3.2.2_216223.json") as f:
#      data7 = json.load(f)
# with open("In_degree_list_IRI_1.4.0_242662.json") as f:
#      data8 = json.load(f)

# data = data2+data3+data4+data5+data6+data7+data8

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.set_yscale('log')
# plt.hist(data,bins = 100,rwidth=0.8)
# plt.axis([-50,1400,0.5,10000000])
# plt.title("S2_In_degree_normalization")
# plt.xlabel('In-Degree num.')
# plt.ylabel('nodes num. ')
# # plt.legend()
# plt.savefig('/Users/fengyangguo/Downloads/S2_In_degree_normalization.png')
# plt.show()
