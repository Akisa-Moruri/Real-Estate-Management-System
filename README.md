# Real-Estate-Management-System
This Python application serves as a Real Estate Management System. It provides functionalities to manage properties, clients, and transactions related to properties.

## Features

## Manage Properties
Add, fetch, update, and delete properties. You can search for properties by ID, location, price range, or type of property.

## Manage Clients
Add, fetch, update, and delete clients. You can also view all clients registered in the system.

## Manage Transactions
Add, fetch, update, and delete transactions. Transactions include activities like buying, selling, or renting properties.


## Installation
1. Clone the repository to your local machine:
```bash
    https://github.com/Akisa-Moruri/Real-Estate-Management-System/tree/main
```
2. Install dependencies:
```bash
    pip install -r requirements.txt
```
## Usage

1. Navigate to the project directory:
```bash
    cd real-estate-management
```
2. Run the application:
```bash
    python main.py
```
3. The application is run from the command line using the `main.py` script. Upon running the script, the application will initialize the database, create the necessary tables, and perform some example operations.

You can modify the `main.py` script to include your desired operations or create additional scripts to interact with the application.

## Project Structure

- Real-Estate-Management-System
    - lib/
        - real_estate.db
    - lib/
        - client.py
        - config.py
        - property.py
        - transaction.py
    - main.py
    - README.md
    
- `lib/real_estate.db`: SQLite database file
- `lib/config.py`: Database configuration and table creation/deletion
- `lib.property`: Handles property-related operations.
- `lib.client`: Manages client-related operations.
- `lib.transaction`: Handles transaction-related operations.
- `main.py`: Entry point of the application
- `README.md`: Project README


## Dependencies
- Python 3.x
- SQLite3 (included in Python standard library)


#### Main Menu Options
- Manage Properties:Options to add, fetch, update, and delete properties.

- Manage clients: Options to add, fetch, update, and delete clients.

- Manage transactions: Options to add, fetch, update, and delete transactions.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## Support and contact details
    - email :: akisamoruri@gmail.com
   

### License
*Licenced under the MIT Licence
Copyright (c) 2024 **Akisa Moruri

