import mysql.connector
from RGSTRLibrary.RGSTRconnect import *

def rgstrimport(filename,datetime):
    configfile="config.ini"
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    inputfile=open(filename)
    linenumber=0
    error=''
    success=0
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
            #print("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
            cursor.execute("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
            cursor.execute("SELECT *\nFROM users\nWHERE CardID=\'{}\';".format(CardID))
            print("SELECT *\nFROM users\nWHERE CardID=\'{}\';".format(CardID))
            row= cursor.fetchall()
            print (row)
            if row==[]:
                conn.rollback()
                error=(error,"\n Error on line:",linenumber,Error)
            else:
                conn.commit()
                #print("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
                cursor.execute("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
                conn.commit()
                success+=1
        except:
            conn.rollback()
            error=(error+str(CardID)+" in database ("+str(linenumber)+")")
    return(str(success)+" Users added\n"+"Errors-\n"+error)


def rgstradd(CardID,Firstname,Lastname,Form,Year,datetime):
    configfile="config.ini"
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    try:
        #print("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
        cursor.execute("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
        cursor.execute("SELECT *\nFROM users;")
        row= cursor.fetchall()
        if row==[]:
            conn.rollback()
        else:
            conn.commit()
            #print("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
            cursor.execute("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
            conn.commit()
    except:
        print("ERROR")
