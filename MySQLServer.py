import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",      
            user="your_username",
            password="your_password"
        )

        cursor = conn.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

    except mysql.connector.Error as err:
        print("Error: Could not connect to the MySQL server.")
        print(f"MySQL Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()
