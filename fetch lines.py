import mysql.connector as msqlcon
mycon = msqlcon.connect(host = "localhost", user = "root", passwd = "040803", database = "db")
if mycon.is_connected() == True:
    print("Successfully connected to mysql database")
crsr = mycon.cursor()
sql1 = crsr.execute("Select * from student")
data = crsr.fetchmany(3)
count = crsr.rowcount
for row in data :
    print(row)
mycon.close()
