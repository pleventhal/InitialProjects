
import MySQLdb
import csv

user = 'pleventhal' # your username
passwd = 'Westlake15' # your password
host = 'depot.westlakefinancial.com' # server name
db = 'risk_dm' # name of the data base

mySqlConn = MySQLdb.connect(host = host, user = user, passwd = passwd, db = db)

# you must create a Cursor object. It will let you execute all the queries you need
cur = mySqlConn.cursor()

query = "SELECT LenderDealerID, Name, WFDealerBookAdvance FROM risk_dm.wfi_recourse_tier"

cur.execute(query)
results = cur.fetchall()
# Close the connection
mySqlConn.close()

fp = open('test.csv', 'w', newline = '\n')
csv.Dialect.lineterminator = '\n'
myFile = csv.writer(fp)
csv.Dialect.delimiter = ''
myArray = ['']

for row in results:
    try:
        myArray[0] = row[1]
        myFile.writerow(row)
    except UnicodeEncodeError:
        print(row[1])

fp.close()

