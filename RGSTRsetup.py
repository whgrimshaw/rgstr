import mysql.connector
input("Start mysql server and press enter")
#CONNECT TO SERVER
try:
    conn=mysql.connector.connect(host="localhost",user="root",passwd="root")
    cursor=conn.cursor()
    print("Connected to MySQL Server")
except:
    print("Unable to connect to server.")
#CREATES DATABASE
try:
    cursor.execute("CREATE DATABASE rgstr;") #creates database on current server
    print ("Database 'rgstr' create successfully")
except:
    print("Database already exists")


#SELECT THE DATABASE
cursor.execute("USE rgstr;")
#CREATES user TABLE
try:
    #print("CREATE TABLE users(\nCardID int NOT NULL PRIMARY KEY,\nFirstname varchar(15),\nLastname varchar(20),\n`Form` varchar (4),\n`Year` int(2));")
    cursor.execute("CREATE TABLE users(\nCardID int NOT NULL PRIMARY KEY,\nFirstname varchar(15),\nLastname varchar(20),\n`Form` varchar (4),\n`Year` int(2));")
    print ("Users table created successfully")
except:
    print ("Users table exists")
#CREATES status TABLE
try:
    #print("CREATE TABLE status(\nCardID int,\nStatus binary(1),\n`DateTime` DateTime,\nFOREIGN KEY(CardID) REFERENCES users(CardID));")
    cursor.execute("CREATE TABLE status(\nCardID int,\nStatus binary(1),\n`DateTime` DateTime,\nFOREIGN KEY(CardID) REFERENCES users(CardID));")
    print ("Status table created successfully")
except:
    print ("Status table exists")


