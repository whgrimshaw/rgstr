import mysql.connector
def databaseconnect():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='rgstr',
                                       user='root',
                                       password='root')
        if conn.is_connected():
            print('Connected to database successfully')
 
    except Error as e:
        print("Connection failed")
        print(e)
