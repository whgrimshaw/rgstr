from RGSTRLibrary.RGSTRconnect import *
from mysql.connector import MySQLConnection, Error
def dbsetup(configfile,cursor):
    #CREATES user TABLE
    try:
        #print("CREATE TABLE users(\nCardID int NOT NULL PRIMARY KEY,\nFirstname varchar(15),\nLastname varchar(20),\n`Form` varchar (4),\n`Year` int(2));")
        cursor.execute("CREATE TABLE users(\nCardID varchar(20) NOT NULL PRIMARY KEY,\nFirstname varchar(15),\nLastname varchar(20),\n`Form` varchar (4),\n`Year` int(2));")
        print ("Users table created successfully")
    except:
        print ("Users table exists")
        #CREATES status TABLE
    try:
        #print("CREATE TABLE status(\nCardID int,\nStatus binary(1),\n`DateTime` DateTime,\nFOREIGN KEY(CardID) REFERENCES users(CardID));")
        cursor.execute("CREATE TABLE status(\nCardID varchar(20),\nStatus binary(1),\n`DateTime` DateTime,\nFOREIGN KEY(CardID) REFERENCES users(CardID));")
        print ("Status table created successfully")
    except:
        print ("Status table exists")
