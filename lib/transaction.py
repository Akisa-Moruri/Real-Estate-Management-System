# Import CONN and CURSOR objects from the 'lib.config' module
from lib.config import CONN, CURSOR


class Transaction:
    # Method to add a new transaction to the database
    @classmethod
    def create_transaction(cls, property_id, amount, date, client_id, transaction_type):
        sql = "INSERT INTO transactions (property_id, amount, date, client_id, transaction_type) VALUES (?, ?, ?, ?, ?)"
        CURSOR.execute(sql, (property_id, amount, date, client_id, transaction_type))
        CONN.commit()
        return CURSOR.lastrowid
    
    # Method to Fetch a transaction by its ID
    @classmethod
    def get_transactions_by_id(cls, property_id):
        sql = "SELECT * FROM transactions WHERE property_id = ?"
        CURSOR.execute(sql, (property_id,))
        return CURSOR.fetchall()
    
    
    # Method to delete a transaction by its ID
    @classmethod
    def delete_transaction_by_id(cls, transaction_id):
        sql = "DELETE FROM transactions WHERE id = ?"
        CURSOR.execute(sql, (transaction_id,))
        CONN.commit()
        return transaction_id
    
    # Method to fetch all transaction from the database
    @classmethod
    def fetch_all_transactions(cls):
        sql = "SELECT * FROM transactions"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    
    
    # Method to Fetch all transaction by a specific client
    #@classmethod
    #def get_transaction_by_client_id(cls, client_id):
    #   sql = "SELECT * FROM transaction WHERE client_id = ?"
    #   CURSOR.execute(sql, (client_id,))
    #   return CURSOR.fetchall()
    
    
    # Method to update a transaction information by its ID
    #@classmethod
    #def update_transaction_by_id(cls, transaction_id, amount, date, transaction_type):
    #    sql = "UPDATE transaction SET amount = ?, date = ?, transaction_type = ? WHERE id = ?"
    #    CURSOR.execute(sql, (amount, date, transaction_type, transaction_id))
    #    CONN.commit()
    #    return transaction_id

    
    
        