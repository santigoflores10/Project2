import sqlite3

def create_empty_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print('creating empty database')
    # Update database settings
    print('Update PRAGMA to support foreign keys')
    cursor.execute('PRAGMA foreign_keys = ON')

    # Drop tables in the correct order 
    print('Drop tables if they exist')
    cursor.execute('DROP TABLE IF EXISTS inventory_needed;')
    cursor.execute('DROP TABLE IF EXISTS customer_party_details;')
    cursor.execute('DROP TABLE IF EXISTS inventory_data;')
    cursor.execute('DROP TABLE IF EXISTS staff_work_hours;')
    cursor.execute('DROP TABLE IF EXISTS staff_details;')
    cursor.execute('DROP TABLE IF EXISTS customer_booking_details;')
    cursor.execute('DROP TABLE IF EXISTS customer_personal_details;')
    cursor.execute('DROP TABLE IF EXISTS customer_financial_records;')

    # Create tables
    print('create customer_financial_records table')
    cursor.execute('''
        CREATE TABLE customer_financial_records (
            Customer_ID INTEGER PRIMARY KEY,
            Bank_Details TEXT(255) NOT NULL,
            Invoices TEXT(100) NOT NULL,
            Payments TEXT(100) NOT NULL
        );
    ''')

    print('create customer_personal_details table')
    cursor.execute('''
        CREATE TABLE customer_personal_details (
            Customer_ID INTEGER PRIMARY KEY,
            First_name TEXT(50),
            Last_name TEXT(50),
            Phone_number INTEGER(15) NOT NULL,
            Postal_address TEXT(255) NOT NULL
        );
    ''')

    print('create customer_booking_details table')
    cursor.execute('''
        CREATE TABLE customer_booking_details (
            Booking_ID INTEGER PRIMARY KEY,
            Customer_ID INTEGER NOT NULL,
            Booking_Date DATE(15) NOT NULL,
            Address TEXT(255) NOT NULL,
            Time TEXT(20) NOT NULL,
            FOREIGN KEY (Customer_ID) REFERENCES customer_personal_details(Customer_ID)
        );
    ''')

    print('create staff_details table')
    cursor.execute('''
        CREATE TABLE staff_details (
            Staff_ID INTEGER PRIMARY KEY,
            Name TEXT(100) NOT NULL,
            Gender TEXT(10),
            Address TEXT(255),
            Phone_Number INTEGER(15) NOT NULL,
            Bank_Details TEXT(255) NOT NULL
        );
    ''')

    print('create staff_work_hours table')
    cursor.execute('''
        CREATE TABLE staff_work_hours (
            Staff_ID INTEGER PRIMARY KEY,
            Num_Events INTEGER(20) NOT NULL,
            Num_Hours INTEGER(5) NOT NULL,
            Travel_Fees REAL(30) NOT NULL,
            FOREIGN KEY (Staff_ID) REFERENCES staff_details(Staff_ID)
        );
    ''')

    print('create inventory_data table')
    cursor.execute('''
        CREATE TABLE inventory_data (
            Inventory_ID INTEGER PRIMARY KEY,
            Supplies TEXT(100) NOT NULL,
            Costume_Inventory TEXT(100) NOT NULL,
            Quantities INTEGER(10) NOT NULL
        );
    ''')

    print('create inventory_needed table')
    cursor.execute('''
        CREATE TABLE inventory_needed (
            Inventory_ID INTEGER NOT NULL,
            Party_ID INTEGER NOT NULL,
            FOREIGN KEY (Inventory_ID) REFERENCES inventory_data(Inventory_ID),
            FOREIGN KEY (Party_ID) REFERENCES customer_party_details(Party_ID),
            PRIMARY KEY (Inventory_ID, Party_ID)
        );
    ''')

    print('create customer_party_details table')
    cursor.execute('''
        CREATE TABLE customer_party_details (
            Party_ID INTEGER PRIMARY KEY,
            Inventory_ID INTEGER NOT NULL,
            Staff_ID INTEGER NOT NULL,
            Booking_ID INTEGER NOT NULL,
            Party_Theme TEXT(100) NOT NULL,
            Character_Requested TEXT(100) NOT NULL,
            Child_name TEXT(50) NOT NULL,
            Age_Turning INTEGER(5) NOT NULL,
            Number_children_Attending INTEGER(15) NOT NULL,
            FOREIGN KEY (Inventory_ID) REFERENCES inventory_data(Inventory_ID),
            FOREIGN KEY (Staff_ID) REFERENCES staff_details(Staff_ID),
            FOREIGN KEY (Booking_ID) REFERENCES customer_booking_details(Booking_ID)
        );
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    print('empty database created')

create_empty_database("party_kids_remember.db")
