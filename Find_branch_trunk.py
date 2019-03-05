import iota
import iotapy
import json

name = "MS11"

r = iotapy.storage.providers.rocksdb.RocksDBProvider(
        # db_path='/home/guo/mainnetdb',
        # db_log_path='/home/guo/mainnetdb.log',

        db_path='/Users/fengyangguo/Downloads/mainnetdb',
        db_log_path='/Users/fengyangguo/Downloads/mainnetdb.log',
        read_only=True
    )
r.init()


file = "MS11_665220.json"
all_nines = '9' * 81
solid_milestone = "RTFSPFNA9ZA9CZVKBCRKYSBMJFAIBKQM9PD9PYAQKZTGULDKINIUOISQTGJP9DVDTPNQJOQKDAH9Z9999"
traversal_queue = [solid_milestone]

# txh = iota.TransactionHash(solid_milestone)
# tx = r.get(txh, 'transaction')

EMPTY = iota.TransactionHash('9' * 81)

tx_list = []
# all_nines_tx = []
memDB = set()

i = 0
with open(file,"w+") as f:
    while traversal_queue:

        tx_hash = traversal_queue.pop()

        if tx_hash in memDB or tx_hash == all_nines:
            # all_nines_tx.append(tx_hash)
            continue

        txh = iota.TransactionHash(tx_hash)
        tx = r.get(txh, 'transaction')
        tx_dict = {}
        # if tx.branch_transaction_hash != EMPTY:
        txb = str(tx.as_json_compatible()['branch_transaction_hash'])
        txt = str(tx.as_json_compatible()['trunk_transaction_hash'])
        address = str(tx.as_json_compatible()['address'])
        txtime = str(tx.timestamp)

        tx_dict["hash"] = tx_hash
        tx_dict["branch_hash"] = txb
        tx_dict["trunk_hash"] = txt
        tx_dict["timestamp"] = txtime
        tx_dict["address"] = address

        tx_list.append(tx_dict)
        # except:
        #     print("error",tx)


        memDB.add(tx_hash)
        traversal_queue.append(txb)
        traversal_queue.append(txt)
        i+=1
        print(i)

        # print(len(tx_list))
    # print(all_nines_tx)
    json.dump(tx_list,f)
pass



