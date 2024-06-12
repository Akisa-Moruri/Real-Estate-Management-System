# Importing necessary classes and modules
from lib.property import Property
from lib.client import Client
from lib.transaction import Transaction
import sys


# Function for main menu
def main_menu():
    while True:
        # Displaying main menu options
        print("=============MAIN MENU=================")
        print("1.Manage properties")
        print("2.Manage clients")
        print("3.Manage transactions")
        print("4.Exit")
        
        # Asking for user input
        choice = input("\nEnter your choice: ")
        if choice == "1":
            property_operations()

        elif choice == "2":
            client_operations()

        elif choice == "3":
            transaction_operations()

        elif choice == "4":
            sys.exit()

        else:
            print("Invalid Input")


# Function for property operations
def property_operations():
    while True:
        # Displaying property menu options
        print("\n*******PROPERTY MENU********")
        print("1.Add new property")
        print("2.Fetch a property by its id")
        print("3.Fetch a property by its location")
        print("4.Update property")
        print("5.Delete a property by its id")
        print("6.Fetch all properties")
        print("7.Search for properties within a price range")
        print("8.Search properties by type of property and size")
        print("9.Return to main menu")
        
        # Asking for user input
        choice = input("\nEnter your choice: ")

        property = Property()
        if choice == "1":
            # Adding a new property
            property_location = input("Enter property location: ")
            price = input("Enter price: ")
            property_type = input("Enter the type of property: ")
            size = input("Enter the size of the property: ")
            
            property_id = property.create_property(property_location, price, property_type, size)
            print(f"Property with id {property_id} added successfully")

        elif choice == "2":
            # Fetching a property by its id
            property_id = input("Enter the id of the property you want to fetch: ")
            single_property = property.get_property_by_id(property_id)
            print(single_property)
            
        elif choice == "3":
            # Fetch a property by its location
            location = input("Enter the location: ")
            single_property = property.get_property_by_location(location)
            if single_property:
                print("Property found at location:", location)
                print("Property details:", single_property)
            else:
                print("Property not found at location:", location)
                
        elif choice == "4":
            # Update a property
            property_id = input("Enter the id of the property you want to update: ")
            property_location = input("Enter the new location: ")
            price = input("Enter the new price: ")
            
            updated_property_id = property.update_property_by_id(property_id, property_location, price)
            print(f"Property with id {updated_property_id} updated successfully")
            
        elif choice == "5":
            # Delete a property by its id
            property_id = input("Enter the id of the property you want to delete: ")
            deleted_property_id = property.delete_property_by_id(property_id)
            print(f"\nProperty {deleted_property_id} deleted successfully")
            
        elif choice == "6":
            # Fetch all properties
            all_properties = property.fetch_all_properties()
            print("\nAll properties")
            print(all_properties)
            
        elif choice == "7":
            # Search for properties within a price range
            min_price = float(input("Enter the minimum price: "))
            max_price = float(input("Enter the maximum price: "))

            found_properties = Property.search_property_by_price_range(min_price, max_price)

            if found_properties:
                print("\nProperties matching the specified criteria:")
                for prop in found_properties:
                    print(prop)
            else:
                print("No properties found matching the specified criteria.")

                
        elif choice == "8":
            # Search properties by type of property and size
            property_type = input("Enter the type of property (e.g., house, apartment): ")

            found_properties = Property.search_property_by_property_type(property_type)

            if found_properties:
                print("\nProperties matching the specified criteria:")
                for prop in found_properties:
                    print(prop)
            else:
                print("No properties found matching the specified criteria.")
                            
        elif choice == "9":
            # Returning to the main menu
            return main_menu()
        
        else:
            print("Invalid Input")           
            
        
            

# Function for client operations
def client_operations():
    while True:
        # Displaying the menu options
        print("\n*******CLIENT MENU********")
        print("1.Adding a client")
        print("2.Delete a client by id")
        print("3.Fetching a client by id")
        print("4.Updating a client")
        print("5.Fetching all clients")
        print("6.Returning to the main menu")
                
        
        # Taking user input for choice
        choice = input("\nEnter your choice: ")

        client = Client()  

        # Adding a client
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")

            created_client_id = client.create_client(name, email)
            print(f"Client {created_client_id} created")
            
            
        # Delete a client by id
        elif choice == "2":
            client_id = input("Enter the id of the client you want to delete: ")
            deleted_client_id = client.delete_client_by_id(client_id)
            print(f"\nClient {deleted_client_id} deleted successfully")
            
            
        
        # Fetching a client by ID
        elif choice == "3":
            client_id = input("Enter client id: ")
            single_client = client.get_client(client_id)
            print("\nFetch client by id ")
            print(single_client)    
        

        # Updating a client
        elif choice == "4":
            client_id = input("Enter client id: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")

            updated_client = client.update_client_by_id(client_id, name, email)
            print(f"\nClient {updated_client} updated")

        # Fetching all clients
        elif choice == "5":
            all_clients = client.fetch_all_clients()
            print("\nAll clients")
            print(all_clients)    
        
                      
        # Returning to the main menu
        elif choice == "6":
            return main_menu()

        # Handling invalid input
        else:
            print("Invalid Input")   
            
            
            
# Function for transaction operations
def transaction_operations():
    while True:
        # Displaying transaction menu options
        print("\n*******TRANSACTION MENU********")
        print("1. Add new transaction")
        print("2. Fetch transactions by property ID")
        print("3. Fetch all transactions")
        print("4. Delete a transaction")
        print("5. Return to main menu")
        
        
        # Get the user's choice
        choice = input("\nEnter your choice: ")
        
        
        # Create an instance of the transaction class
        transaction = Transaction()
        
        # Add a new transaction
        if choice == "1":
                property_id = input("Enter property id: ")
                amount = input("Enter amount: ")
                date = input("Enter date (YYYY-MM-DD): ")
                client_id = input("Enter client id: ")
                transaction_type = input("Enter transaction type: ")
                transaction_id = transaction.create_transaction(property_id, amount, date, client_id, transaction_type)
                print(f"\nTransaction {transaction_id} created")

        
        # Fetch transactions by property ID
        elif choice == "2":
                property_id = input("Enter property id: ")
                transactions_by_property_id = transaction.get_transactions_by_id(property_id)
                print("\nTransactions by property ID:")
                print(transactions_by_property_id)
                
                
        # Fetch all transactions
        elif choice == "3":
            all_transactions = transaction.fetch_all_transactions()
            print("\nAll transactions")
            print(all_transactions)
            
        # Delete a transaction by ID
        elif choice == "4":
            transaction_id = input("Enter transaction id: ")
            deleted_transaction_id = transaction.delete_transaction_by_id(transaction_id)
            print(f"\nTransaction {deleted_transaction_id} deleted successfully")
            
            
        # Return to the main menu
        elif choice == "5":
            return main_menu()
        
        else:
            print("Invalid Input")
# Call the main menu function
main_menu()


       