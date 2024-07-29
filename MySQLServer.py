import mysql.connector

host = "127.0.0.1"
user = "root"
password = "0924475152@os"

try:
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    cursor = db.cursor()

    cursor.execute("SHOW DATABASES;")
    databases = [db[0] for db in cursor]
    if "alx_book_store" in databases:
        print("Database 'alx_book_store' already exists.")
    else:
        cursor.execute("CREATE DATABASE alx_book_store;")
        print("Database 'alx_book_store' created successfully!")

    cursor.close()
    db.close()

except mysql.connector.Error as e:
    print(f"Error occurred: {e}")