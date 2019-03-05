import pymysql

db = pymysql.connect(database = 'IOTA_Snapshots', user = 'nmt_fg',
password = 'fineblanking',host = 'wzl-sql2', port = 1436 )

cursor = db.cursor()

# db.commit()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)


