from RGSTRconnect import *
import datetime
def databaselookup(UID,configfile):
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT users.Firstname,users.Lastname,status.Status\nFROM users,status\nWHERE users.CardID=\'%u\'\nAND users.CardID=status.CardID;"%(UID))
        #cursor.execute("SELECT *\nFROM users\nWHERE CardID=\'%u\';"%(UID))
        #cursor.execute("SELECT*\nFROM users;")
        row= cursor.fetchall()
        if row==[]:
            pass
        else:
            return row
    except:
        print("Error: Invalid Card UID")

def updatestatus(UID,status,configfile):
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    Datetime=datetime.datetime.now()
    if status=="1":
        newstatus=0   
    else:
        newstatus=1
    cursor.execute("UPDATE status\nSET CardID=\'{}\',Status=\'{}\',DateTime=\'{}\'\nWHERE CardID=\'{}\';".format(UID,newstatus,Datetime,UID))
    print(newstatus)
    conn.commit()
