import mysql.connector
from RGSTRconnect import *

def rgstradd(filename,datetime):
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
            print("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
            cursor.execute("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
            cursor.execute("SELECT *\nFROM users;")
            row= cursor.fetchall()
            if row==[]:
                conn.rollback()
                error=(error,"\n Error on line:",linenumber,Error)
            else:
                conn.commit()
                print("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
                cursor.execute("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
                conn.commit()
                success+=1
            
                
        except:
            error=(error,"\n Error on line:",linenumber,Error)
    return(success,"users were added to the database\n\n",error)
def rgstradd1(filename,datetime):
    configfile="config.ini"
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    error=''
    success=0
    try:
        #print("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
        cursor.execute("INSERT INTO users\nVALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(CardID,Firstname,Lastname,Form,Year))
        cursor.execute("SELECT *\nFROM users;")
        row= cursor.fetchall()
        if row==[]:
            conn.rollback()
            error=(error,"\n Error on line:",linenumber,Error)
        else:
            conn.commit()
            #print("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
            cursor.execute("INSERT INTO status\nVALUES(\'{}\',\'1\',\'{}\');".format(CardID,datetime))
            conn.commit()
    except:
        error=(error,"\n Error on line:",linenumber,Error)
    print(success,"users were added to the database\n\n",error)
