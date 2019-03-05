import json

with open("MS9_milestone_dict_correct.json") as f:
    data = json.load(f)

for i in data:
    if i["index"] in [417696,412004,414218,416750,416175,410934]:
        print(i)


# new_data = []
#
# for i in data:
#     if i["hash"] == "INECWASLVBC9TQIACEOAXRCTOGTQPVUCLXDLY99999999999999999999999999999999999999999999":
#         correct_milestone = {}
#         correct_milestone["index"] = 417696
#         correct_milestone["hash"] = "INECWASLVBC9TQIACEOAXRCTOGTQPVUCLXDLGPEINTBPCERSQCST9RCJVBHONIYTC9STQCFCFJcoFLZ9999"
#         correct_milestone["trunk_hash"] = "DRJIVAJXRGAXNFJPXSRDDDBDSZVZSUKVMJFEGMQJMYRVS9TNLGWLGQXRBVEWBGSVRKVGNFNOPWYOZ9999"
#         correct_milestone["branch_hash"] = "RXITREWNEF9TPAEITCCSID9KNRYBRGLJOKXUGWBMGIEFAGB9PGYYR9EYJGZMDKPRWGSGOTNWJBXDA9999"
#         correct_milestone["timestamp"] = "1524416362"
#         new_data.append(correct_milestone)
#     elif i["hash"] == "IIRPZSYIEYMLAYELIT9E9999999999999999999999999999999999999999999999999999999999999":
#         correct_milestone = {}
#         correct_milestone["index"] = 412004
#         correct_milestone["hash"] = "IIRPZSYIEYMLAYELIT9ELILSSPWXYVUBYAXGRLGSIBQOGTEUIRVWRNJMPXWME9EABLGCLTZIOVBOZ9999"
#         correct_milestone["trunk_hash"] = i["trunk_hash"]
#         correct_milestone["branch_hash"] = i["branch_hash"]
#         correct_milestone["timestamp"] = i["timestamp"]
#         new_data.append(correct_milestone)
#     elif i["hash"] == "YATPPZATOCPTRDMMKTCKZYO9XHDVZPIC99OURASRESJDAYBJKFKA9XL99999999999999999999999999":
#         correct_milestone = {}
#         correct_milestone["index"] = 414218
#         correct_milestone["hash"] = "YATPPZATOCPTRDMMKTCKZYO9XHDVZPIC99OURASRESJDAYBJKFKA9XLT9QKEBMFQMXHRKOHWFVZP99999"
#         correct_milestone["trunk_hash"] = i["trunk_hash"]
#         correct_milestone["branch_hash"] = i["branch_hash"]
#         correct_milestone["timestamp"] = i["timestamp"]
#         new_data.append(correct_milestone)
#     elif i["hash"] == "HHNPCPVQSGNMLJA9IKOL9ZOYERC999999999999999999999999999999999999999999999999999999":
#         correct_milestone = {}
#         correct_milestone["index"] = 416750
#         correct_milestone["hash"] = "HHNPCPVQSGNMLJA9IKOL9ZOYERUWARRYTLCPGPBCDQRWLVOWTCXMKQDIJORQLHUW9LFFETYINMD999999"
#         correct_milestone["trunk_hash"] = i["trunk_hash"]
#         correct_milestone["branch_hash"] = i["branch_hash"]
#         correct_milestone["timestamp"] = i["timestamp"]
#         new_data.append(correct_milestone)
#     elif i["hash"] == "E9AQDRHSABRBVCNRJIWRJCUMGAEUNCMPLPPBO9ZIL9PKMQY9999999999999999999999999999999999":
#         correct_milestone = {}
#         correct_milestone["index"] = 416175
#         correct_milestone["hash"] = "E9AQDRHSABRBVCNRJIWRJCUMGAEUNCMPLPPBO9ZIL9PKMQGCWTNJMCMCWMLVMWWWWORFJSCIQYWN99999"
#         correct_milestone["trunk_hash"] = i["trunk_hash"]
#         correct_milestone["branch_hash"] = i["branch_hash"]
#         correct_milestone["timestamp"] = i["timestamp"]
#         new_data.append(correct_milestone)
#     elif i["hash"] == "UKXFBGOGLUM99QAVQWPZYIYEKUAQCSDTUUUGRBFPUC999999999999999999999999999999999999999":
#         correct_milestone = {}
#         correct_milestone["index"] = 410934
#         correct_milestone["hash"] = "UKXFBGOGLUM99QAVQWPZYIYEKUAQCSDTUUUGRBFPUUSJVWNURGZSLZVTGAEOIWYUMYZAZEUMIJXUA9999"
#         correct_milestone["trunk_hash"] = i["trunk_hash"]
#         correct_milestone["branch_hash"] = i["branch_hash"]
#         correct_milestone["timestamp"] = i["timestamp"]
#         new_data.append(correct_milestone)
#     else:
#         new_data.append(i)
# print(len(data))
# print(len(new_data))
#
# with open("MS9_milestone_dict_correct.json","w") as f:
#     json.dump(new_data,f)
