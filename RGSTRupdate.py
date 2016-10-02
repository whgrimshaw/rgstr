from RGSTRconnect import *

def databaselookup(UID,configfile):
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT users.CardID,status.Status\nFROM users,status\nWHERE users.CardID=\'%u\'\nAND users.CardID=status.CardID;"%(UID))
        #cursor.execute("SELECT *\nFROM users\nWHERE CardID=\'%u\';"%(UID))
        row= cursor.fetchall()
        if row==[]:
            print("Card is not registered")
        else:
            return row
    except:
        print("Error: Invalid Card UID")
