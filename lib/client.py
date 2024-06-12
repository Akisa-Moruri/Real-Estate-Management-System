# Import CONN and CURSOR objects from the 'lib.config' module
from lib.config import CONN, CURSOR


class Client:
    # Method to add a new client to the database
    @classmethod
    def create_client(cls, name, email):
        sql = "INSERT INTO client(name, email) VALUES (?, ?)"
        CURSOR.execute(sql, (name, email))
        CONN.commit()
        return CURSOR.lastrowid
    
    # Method to retrieve a client by their ID
    @classmethod
    def get_client(cls, client_id):
        sql = "SELECT * FROM client WHERE id = ?"
        CURSOR.execute(sql, (client_id,))
        return CURSOR.fetchone()
    
    # Method to update client information by their ID
    @classmethod
    def update_client_by_id(cls, client_id, name, email):
        sql = "UPDATE client SET location = ?, email = ? WHERE id = ?"
        CURSOR.execute(sql, (name, email, client_id))
        CONN.commit()
        return client_id
    
    # Method to delete a client by their ID
    @classmethod
    def delete_client_by_id(cls, client_id):
        sql = "DELETE FROM client WHERE id = ?"
        CURSOR.execute(sql, (client_id,))
        CONN.commit()
        return client_id
    
    # Method to fetch all client from the database
    @classmethod
    def fetch_all_client(cls):
        sql = "SELECT * FROM client"
        CURSOR.execute(sql)
        return CURSOR.fetchall()