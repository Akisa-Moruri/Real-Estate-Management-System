# Import the sqlite3 module to work with SQLite databases
import sqlite3

# Connect to the 'real_estate.db' database file
CONN = sqlite3.connect('real_estate.db')

# Create a cursor object to execute SQL queries
CURSOR = CONN.cursor()


class Database:
    def create_tables(self):
        # SQL query to create the 'property' table
        sql1 = """
            CREATE TABLE IF NOT EXISTS property (
            id INTEGER PRIMARY KEY,
            property_location TEXT(40),
            price INTEGER,
            property_type TEXT,
            size varchar(40))"""
        
        # SQL query to create the 'client' table
        sql2 = """
            CREATE TABLE IF NOT EXISTS client(
            id INTEGER PRIMARY KEY,
            name varchar (40),
            email varchar (40))"""
        
        # SQL query to create the 'transaction' table
        sql3 = """
            CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY,
            amount INTEGER,
            date varchar (40),
            property_id INTEGER,
            client_id INTEGER,
            transaction_type TEXT,
            FOREIGN KEY(property_id) REFERENCES property(id),
            FOREIGN KEY(client_id) REFERENCES client(id))"""
        
        # Execute all SQL queries
        CURSOR.execute(sql1)
        CURSOR.execute(sql2)
        CURSOR.execute(sql3)
        
        # Commit the transaction
        CONN.commit()
        
    def drop_tables(self):
        # SQL queries to drop the tables if they exist
        sql1 = """DROP TABLE IF EXISTS property"""
        sql2 = """DROP TABLE IF EXISTS client"""
        sql3 = """DROP TABLE IF EXISTS transactions"""
        
        # Execute all SQL queries
        CURSOR.execute(sql1)
        CURSOR.execute(sql2)
        CURSOR.execute(sql3)
        
        # Commit the transaction
        CONN.commit()
        
# Instantiate the Database class
db = Database()

# Call the create_tables method
db.create_tables()
# db.drop_tables()

# Close the database connection
# CONN.close()
