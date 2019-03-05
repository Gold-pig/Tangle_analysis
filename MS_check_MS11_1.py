import json

def milestone_list(name):


    with open('{}.json'.format(name)) as f:
            data = json.load(f)

    with open('MS11_milestone_dict.json') as f:
            all_milestone = json.load(f)

    hash_d = {}
    idata = []
    sub_snapshot_mile_theory = []
    sub_snapshot_mile = []
    hash_list = []

    for i in all_milestone:
        sub_snapshot_mile_theory.append(int(i["index"]))

    for idx,item in enumerate(all_milestone):
        hash_d[item["hash"]] = item["index"]
        idata.append(item)
    for i in data:
        hash_list.append(i["hash"])

    for i in hash_list:
        if i in hash_d.keys():
            sub_snapshot_mile.append(hash_d[i])

    Diff = list(set(sub_snapshot_mile_theory).difference(set(sub_snapshot_mile)))
    print(Diff)



    # for idx,item in enumerate(data):
    #     if item["hash"] in hash_d:
    #         milestone_dict = {}
    #         milestone_dict["idx"] = idx
    #         milestone_dict["hash"] = item["hash"]
    #         milestone.append(milestone_dict)


milestone_list(name="MS11_1")



