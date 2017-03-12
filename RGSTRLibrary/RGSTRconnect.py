from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
from RGSTRLibrary.RGSTRsetup import *
#PARSES AND IMPORTS EXTERNAL CONFIG FILE- FORMATTED AS AN ARRAY
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
#ATTEMPTS TO ESTABLISH A CONNECTION BETWEEN THE PROGRAM AND THE DATABASE SERVER
def databaseconnect(configfile):
    db_config=readconfig(configfile)
    try:
        print('Connecting to MySQL database...')
        conn=MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
            return conn
        else:
            print('Connection failed.')
    except Error as error:
        print (error)
