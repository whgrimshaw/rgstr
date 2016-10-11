from RGSTRconnect import *

def databaselookup(UID,configfile):
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    try:
        #cursor.execute("SELECT users.Firstname,users.Lastname,status.Status\nFROM users,status\nWHERE users.CardID=\'%u\'\nAND users.CardID=status.CardID;"%(UID))
        #cursor.execute("SELECT *\nFROM users\nWHERE CardID=\'%u\';"%(UID))
        cursor.execute("SELECT*\nFROM users;")
        row= cursor.fetchall()
        if row==[]:
            pass
        else:
            return row
    except:
        print("Error: Invalid Card UID")
