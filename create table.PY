import mysql.connector as msqlcon
mycon = msqlcon.connect(host = "localhost", user = "root", passwd = "040803", database = "db")
if mycon.is_connected() == True:
    print("Successfully connected to mysql database")
crsr = mycon.cursor()
sql_comm = crsr.execute("Create table student(Rollno int(10), Name varchar(20), Marks int(10))")
print("Table created")
mycon.commit()
mycon.close()
