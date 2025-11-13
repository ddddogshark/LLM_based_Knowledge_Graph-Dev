# src/database/mysql_driver.py

import mysql.connector
from src.config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

class MySQLDriver:
    def __init__(self):
        self.host = MYSQL_HOST
        self.port = MYSQL_PORT
        self.user = MYSQL_USER
        self.password = MYSQL_PASSWORD
        self.database = MYSQL_DB
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print(f"Successfully connected to MySQL database: {self.database}")
            return self.connection
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")

    def execute_query(self, query: str, params: tuple = None, fetch_one: bool = False, fetch_all: bool = False):
        if not self.connection or not self.connection.is_connected():
            print("No active MySQL connection. Attempting to reconnect...")
            self.connect()
            if not self.connection or not self.connection.is_connected():
                print("Failed to establish MySQL connection.")
                return None

        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                if fetch_one:
                    return cursor.fetchone()
                elif fetch_all:
                    return cursor.fetchall()
                else:
                    return None # Or raise an error if fetch_one/fetch_all is expected
            else:
                self.connection.commit()
                return cursor.rowcount
        except mysql.connector.Error as e:
            print(f"Error executing MySQL query: {e}")
            self.connection.rollback()
            return None
        finally:
            cursor.close()

# Example usage (for testing purposes)
if __name__ == "__main__":
    mysql_driver = MySQLDriver()
    connection = mysql_driver.connect()

    if connection:
        # Example: Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS raw_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            source VARCHAR(255),
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        print(f"Creating table: {create_table_query}")
        mysql_driver.execute_query(create_table_query)

        # Example: Insert data
        insert_query = "INSERT INTO raw_data (source, content) VALUES (%s, %s)"
        data_to_insert = ("test_source", "This is some raw content from a test.")
        print(f"Inserting data: {data_to_insert}")
        mysql_driver.execute_query(insert_query, data_to_insert)

        # Example: Select data
        select_query = "SELECT * FROM raw_data"
        print(f"Selecting data: {select_query}")
        results = mysql_driver.execute_query(select_query, fetch_all=True)
        if results:
            for row in results:
                print(row)
        else:
            print("No data found.")

        mysql_driver.disconnect()
