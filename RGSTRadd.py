import mysql.connector
from RGSTRconnect import *
def rgstradd(filename):
    configfile="config.ini"
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
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
            cursor.execute("USE rgstr")
            cursor.execute("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
            cursor.execute("SELECT *\nFROM users;")
            row= cursor.fetchall()
            if row==[]:
                conn.rollback()
                return("There has been an error\n\n",Error)
            else:
                conn.commit()
                
        except:
            return("There has been an error\n\n",Error)
    return(linenumber,"users were added to the database")
