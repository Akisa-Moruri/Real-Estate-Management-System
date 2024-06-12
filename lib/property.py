# Import CONN and CURSOR objects from the 'lib.config' module
from lib.config import CONN, CURSOR


# Import CONN and CURSOR objects from the 'lib.config' module
from lib.config import CONN, CURSOR


class Property:
    # Method to add a new property to the database
    @classmethod
    def create_property(cls, property_location, price, property_type):
        sql = "INSERT INTO property(property_location, price, property_type) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (property_location, price, property_type))
        CONN.commit()
        return CURSOR.lastrowid
    
    # Method to fetch a property by its ID
    @classmethod
    def get_property_by_id(cls, property_id):
        sql = "SELECT * FROM property WHERE id = ?"
        CURSOR.execute(sql, (property_id,))
        return CURSOR.fetchone()
    
    # Method to fetch a property by its Location
    @classmethod
    def get_property_by_location(cls, property_location):
        sql = "SELECT * FROM property WHERE property_location = ?"
        CURSOR.execute(sql, (property_location,))
        return CURSOR.fetchone()
    
    # Method to update property information by its ID
    @classmethod
    def update_property_by_id(cls, property_id, property_location, price):
        sql = "UPDATE property SET property_location = ?, price = ? WHERE id = ?"
        CURSOR.execute(sql, (property_location, price, property_id))
        CONN.commit()
        return property_id
    
    # Method to delete a property by its ID
    @classmethod
    def delete_property_by_id(cls, property_id):
        sql = "DELETE FROM property WHERE id = ?"
        CURSOR.execute(sql, (property_id,))
        CONN.commit()
        return property_id
    
    # Method to fetch all property from the database
    @classmethod
    def fetch_all_properties(cls):
        sql = "SELECT * FROM property"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    # Method to search for property within a price range
    @classmethod
    def search_property_by_price_range(cls, min_price, max_price):
        sql = "SELECT * FROM property WHERE price BETWEEN ? AND ?"
        CURSOR.execute(sql, (min_price, max_price))
        return CURSOR.fetchall()
    
    @classmethod
    # Method to search property by property type
    def search_property_by_property_type(cls, property_type):
        sql = "SELECT * FROM property WHERE property_type = ?"
        CURSOR.execute(sql, (property_type,))
        return CURSOR.fetchall()
