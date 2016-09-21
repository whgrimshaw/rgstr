from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

def readconfig(configfile,section='mysql'):
    parser=ConfigParser()
    parser.read(configfile)
    db={}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        print("Error reading config file- section doesnt exist")
    return (db)

def databaseconnect(configfile):
    db_config=readconfig(configfile)
    try:
        print('Connecting to MySQL database...')
        conn=MySQLConnection(**db_config)
 
        if conn.is_connected():
            print('connection established.')
            return conn
        else:
            print('connection failed.')
        
 
    except Error as error:
        print(error)

def databaselookup(UID,configfile):
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT *\nFROM users\nWHERE CardID=\'%u\'"%(UID))
        row= cursor.fetchall()
        if row==[]:
            print("Card is not registered")
        else: 
            print (row)
    except:
        print("Error: Invalid Card UID")
        
    
