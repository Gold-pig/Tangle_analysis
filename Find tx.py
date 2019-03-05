import iota
import iotapy
import json

name = "MS10"

r = iotapy.storage.providers.rocksdb.RocksDBProvider(
        db_path='/Users/fengyangguo/Downloads/mainnetdb',
        db_log_path='/Users/fengyangguo/Downloads/mainnetdb.log',
        read_only=True
    )
r.init()


# txh = iota.TransactionHash('XIYGZCYYDXIJIBBHJBFXGGFBXWA9PMKBATYZLSPIPDVRADGRXWIAIYVNUZODOJCORSIDXDIZPCJZA9999')
# column_family = 'transaction'
# tx = r.get(txh, column_family)
# tx.tag
# print(tx.tag)

# adr = iota.Address('KPWCHICGJZXKE9GSUDXZYUAPLHAKAHYHDXNPHENTERYMMBQOPSQIDENXKLKCEYCPVTZQLEEJVYJZV9BWU')
# r.get(adr,'address')
# print(r.get(adr,'address'))
# print(list(r.get(adr,'address')))
# print(len(list(r.get(adr,'address'))))

r.first('milestone')
print(r.first('milestone'))
genesis = []

# print(r.next(243001,'milestone'))

def milestone_list(num):
    milestone_dict = {}
    milestone = []
    # milestone.append(r.first('milestone'))
    # num = 243000
    while num <=774803:
        if num<=774803:
            # print(r.next(num,'milestone')[1])
            milestone_dict = {}
            milestone_dict['index'] = r.next(num,'milestone')[0]
            milestone_dict['hash'] = str(r.next(num,'milestone')[1][1])
            # milestone_str = str(r.next(num,'milestone')[1][1])
            txh = iota.TransactionHash(str(r.next(num,'milestone')[1][1]))
            column_family = 'transaction'
            tx = r.get(txh, column_family)
            milestone_dict['trunk_hash'] = str(tx.trunk_transaction_hash)
            milestone_dict['branch_hash'] = str(tx.branch_transaction_hash)
            if str(tx.branch_transaction_hash) == "999999999999999999999999999999999999999999999999999999999999999999999999999999999":
                genesis.append(milestone_dict)
            print(milestone_dict)
            # milestone_dict[r.next(num,'milestone')[1][0]] = milestone_str
            milestone.append(milestone_dict)
        num = num + 1
    # print(milestone_dict)
    # print(milestone)
    # print(milestone_dict.keys())
    # print(milestone_dict.values())
    # print(len(list(milestone_dict.values())[1]))


    #
    # with open("/Users/fengyangguo/PycharmProjects/Tangle_data_analysis/milestone_dataset/{n}_milestone_dict.json".format(n = name),"w") as f:
    #     json.dump(genesis,f)
    #     # f.write("{}".format(milestone))
    #     f.flush()

    return milestone

milestone_list(590000)


# with open("{n}_milestone_list.txt".format(n = name),"w") as f:
#     f.write("{}".format(milestone_list(243000)))



# with open("{n}_milestone_list.txt".format(n = name),"w") as f:
#     json.dump(list(r.get(adr,'address')),f)
