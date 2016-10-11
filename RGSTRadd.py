import mysql.connector
from RGSTRconnect import *
input("Start mysql server and press enter")
configfile="config.ini"
conn=databaseconnect(configfile)
cursor=conn.cursor()
filename=("users.csv")
inputfile=open(filename)
linenumber=0
for line in inputfile:
    linenumber+=1
    print("Line Number:",linenumber)
    i=line.split(",")
    CardID=i[0]
    Firstname=i[1]
    Lastname=i[2]
    Form=i[3]
    Year=i[4]
    print (CardID)
    print(Firstname)
    print(Lastname)
    print(Form)
    print(Year)
    try:
        conn=databaseconnect(configfile)
        cursor=conn.cursor()
        cursor.execute("USE rgstr")
        cursor.execute("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
        cursor.execute("SELECT *\nFROM users;")
        row= cursor.fetchall()
        if row==[]:
            print(Error)
        else:
            print(row)
    except:
        print(Error)
