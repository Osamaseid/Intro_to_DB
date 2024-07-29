import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='0924475152@os'
        )
        
        cursor = conn.cursor()
        
    
        try:
            cursor.execute("CREATE DATABASE alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print("Database 'alx_book_store' already exists.")
            else:
                print(f"Failed creating database: {err}")
        
        cursor.close()
        conn.close()
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if __name__ == "__main__":
    create_database()
