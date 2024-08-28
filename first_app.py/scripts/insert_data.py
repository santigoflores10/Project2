import sqlite3

def insert_sample_data(database_name):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    print('Inserting data into database')

    # Inserting data into customer_personal_details table
    print('Inserting data into customer_personal_details table')
    customers = [
        (1, "Stephanie", "Brown", 1234567890, "123 Elm Street, Springfield"),
        (2, "Mark", "Smith", 9876543210, "456 Oak Avenue, Metropolis"),
        (3, "Liam", "Johnson", 5556667777, "789 Maple Road, Gotham"),
        (4, "Olivia", "Williams", 1231231234, "101 Pine Street, Star City"),
        (5, "Noah", "Davis", 9879879870, "202 Cedar Avenue, Central City"),
        (6, "Emma", "Martinez", 5555555555, "303 Birch Lane, Coast City"),
        (7, "Sophia", "Lopez", 2223334444, "401 Spruce Street, Gotham"),
        (8, "James", "Wilson", 4445556666, "501 Oak Avenue, Metropolis"),
        (9, "Mia", "Taylor", 6667778888, "601 Maple Road, Star City"),
        (10, "Lucas", "Harris", 7778889999, "701 Birch Lane, Springfield"),
        (11, "Charlotte", "Clark", 8889990000, "801 Pine Street, Coast City"),
        (12, "Amelia", "Lee", 9990001111, "901 Cedar Avenue, Central City"),
        (13, "Ethan", "Morris", 1112223333, "1001 Oak Avenue, Metropolis"),
        (14, "Ava", "Walker", 2223334445, "1101 Maple Road, Gotham"),
        (15, "William", "Hall", 3334445556, "1201 Pine Street, Springfield"),
        (16, "Isabella", "Young", 4445556667, "1301 Birch Lane, Star City")
    ]
    cursor.executemany('INSERT INTO customer_personal_details (Customer_ID, First_name, Last_name, Phone_number, Postal_address) VALUES (?, ?, ?, ?, ?);', customers)

    # Inserting data into customer_financial_records table
    print('Inserting data into customer_financial_records table')
    financial_records = [
        (1, "Bank of Springfield, 123456789", "INV-1001", "669"),
        (2, "Metropolis Bank, 987654321", "INV-1002", "909"),
        (3, "Gotham Credit Union, 555666777", "INV-1003", "103"),
        (4, "Star City Bank, 111222333", "INV-1004", "404"),
        (5, "Central City Credit Union, 444555666", "INV-1005", "832"),
        (6, "Coast City Savings, 777888999", "INV-1006", "1007"),
        (7, "Gotham Bank, 333444555", "INV-1007", "517"),
        (8, "Metropolis Credit Union, 222333444", "INV-1008", "611"),
        (9, "Springfield Savings, 444555666", "INV-1009", "710"),
        (10, "Star City Credit Union, 555666777", "INV-1010", "805"),
        (11, "Central City Bank, 666777888", "INV-1011", "902"),
        (12, "Coast City Credit Union, 111222333", "INV-1012", "1103"),
        (13, "Gotham Savings, 777888999", "INV-1013", "1205"),
        (14, "Metropolis Savings, 333444555", "INV-1014", "1333"),
        (15, "Springfield Credit Union, 999000111", "INV-1015", "1450"),
        (16, "Star City Savings, 222333444", "INV-1016", "1520")
    ]
    cursor.executemany('INSERT INTO customer_financial_records (Customer_ID, Bank_Details, Invoices, Payments) VALUES (?, ?, ?, ?);', financial_records)

    # Inserting data into customer_booking_details table
    print('Inserting data into customer_booking_details table')
    bookings = [
        (1, 1, "2024-08-15", "123 Elm Street, Springfield", "14:00"),
        (2, 2, "2024-09-01", "456 Oak Avenue, Metropolis", "10:00"),
        (3, 3, "2024-09-20", "789 Maple Road, Gotham", "16:00"),
        (4, 4, "2024-10-05", "101 Pine Street, Star City", "11:00"),
        (5, 5, "2024-11-12", "202 Cedar Avenue, Central City", "13:00"),
        (6, 6, "2024-12-18", "303 Birch Lane, Coast City", "15:00"),
        (7, 7, "2024-07-23", "401 Spruce Street, Gotham", "10:30"),
        (8, 8, "2024-08-30", "501 Oak Avenue, Metropolis", "09:00"),
        (9, 9, "2024-09-15", "601 Maple Road, Star City", "15:30"),
        (10, 10, "2024-10-10", "701 Birch Lane, Springfield", "12:00"),
        (11, 11, "2024-11-25", "801 Pine Street, Coast City", "14:30"),
        (12, 12, "2024-12-30", "901 Cedar Avenue, Central City", "16:15"),
        (13, 13, "2025-01-10", "1001 Oak Avenue, Metropolis", "11:45"),
        (14, 14, "2025-02-05", "1101 Maple Road, Gotham", "13:30"),
        (15, 15, "2025-03-15", "1201 Pine Street, Springfield", "09:15"),
        (16, 16, "2025-04-20", "1301 Birch Lane, Star City", "14:45")
    ]
    cursor.executemany('INSERT INTO customer_booking_details (Booking_ID, Customer_ID, Booking_Date, Address, Time) VALUES (?, ?, ?, ?, ?);', bookings)

    # Inserting data into customer_party_details table
    print('Inserting data into customer_party_details table')
    parties = [
        (1, 12, 101, 1, "Superheroes", "Spider-Man", "Johnny", 7, 10),
        (2, 13, 102, 2, "Princesses", "Elsa", "Emma", 5, 8),
        (3, 14, 103, 3, "Pirates", "Jack Sparrow", "Chris", 6, 12),
        (4, 15, 104, 4, "Dinosaurs", "T-Rex", "Lucas", 4, 15),
        (5, 16, 105, 5, "Space", "Buzz Lightyear", "Sophia", 9, 7),
        (6, 17, 106, 6, "Fairy Tales", "Cinderella", "Ava", 5, 10),
        (7, 18, 107, 7, "Superheroes", "Batman", "Mason", 8, 12),
        (8, 19, 108, 8, "Circus", "Clown", "Ella", 6, 14),
        (9, 20, 109, 9, "Animals", "Lion", "Jack", 7, 11),
        (10, 21, 110, 10, "Magic", "Magician", "Emily", 9, 9),
        (11, 22, 111, 11, "Science", "Mad Scientist", "Sophia", 10, 10),
        (12, 23, 112, 12, "Cars", "Lightning McQueen", "Henry", 4, 7),
        (13, 24, 113, 13, "Knights", "King Arthur", "Oliver", 5, 13),
        (14, 25, 114, 14, "Space", "Astronaut", "Charlotte", 9, 12),
        (15, 26, 115, 15, "Jungle", "Tarzan", "Ella", 6, 15),
        (16, 27, 116, 16, "Adventure", "Indiana Jones", "Benjamin", 8, 10)
    ]
    cursor.executemany('INSERT INTO customer_party_details (Party_ID, Inventory_ID, Staff_ID, Booking_ID, Party_Theme, Character_Requested, Child_name, Age_Turning, Number_children_Attending) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);', parties)

    # Inserting data into staff_details table
    print('Inserting data into staff_details table')
    staff = [
        (101, "Alice", "Female", "789 Pine Street, Springfield", 1234567890, "Bank of Springfield, 987654321"),
        (102, "Bob", "Male", "101 Cedar Lane, Metropolis", 9876543210, "Metropolis Bank, 1122334455"),
        (103, "Charlie", "Male", "202 Birch Boulevard, Gotham", 5556667777, "Gotham Credit Union, 6677889900"),
        (104, "Diana", "Female", "404 Maple Drive, Star City", 4444444444, "Star City Bank, 2233445566"),
        (105, "Ethan", "Male", "505 Oak Lane, Central City", 3333333333, "Central City Credit Union, 3344556677"),
        (106, "Fiona", "Female", "606 Birch Road, Coast City", 2222222222, "Coast City Savings, 5566778899"),
        (107, "Grace", "Female", "707 Oak Avenue, Metropolis", 1111111111, "Metropolis Bank, 2233445566"),
        (108, "Henry", "Male", "808 Pine Street, Gotham", 2223334444, "Gotham Bank, 3344556677"),
        (109, "Ivy", "Female", "909 Maple Road, Springfield", 3334445555, "Springfield Credit Union, 4455667788"),
        (110, "Jack", "Male", "1000 Birch Lane, Star City", 4445556666, "Star City Credit Union, 5566778899"),
        (111, "Kate", "Female", "1101 Oak Avenue, Central City", 5556667777, "Central City Bank, 6677889900"),
        (112, "Liam", "Male", "1202 Pine Street, Metropolis", 6667778888, "Metropolis Credit Union, 7788990011"),
        (113, "Mia", "Female", "1303 Birch Lane, Gotham", 7778889999, "Gotham Savings, 8899001122"),
        (114, "Nina", "Female", "1404 Maple Road, Coast City", 8889990000, "Coast City Savings, 9900112233"),
        (115, "Owen", "Male", "1505 Pine Street, Star City", 9990001111, "Star City Savings, 1100223344"),
        (116, "Piper", "Female", "1606 Birch Lane, Springfield", 1112223333, "Springfield Savings, 1211223344")
    ]
    cursor.executemany('INSERT INTO staff_details (Staff_ID, Name, Gender, Address, Phone_Number, Bank_Details) VALUES (?, ?, ?, ?, ?, ?);', staff)

    # Inserting data into staff_work_hours table
    print('Inserting data into staff_work_hours table')
    work_hours = [
        (101, 10, 50, 100.50),
        (102, 8, 40, 80.00),
        (103, 12, 60, 120.75),
        (104, 15, 75, 150.00),
        (105, 9, 45, 90.25),
        (106, 11, 55, 110.50),
        (107, 13, 65, 130.75),
        (108, 9, 45, 90.00),
        (109, 14, 70, 140.00),
        (110, 10, 50, 100.50),
        (111, 12, 60, 120.75),
        (112, 13, 65, 130.75),
        (113, 9, 45, 90.00),
        (114, 14, 70, 140.00),
        (115, 10, 50, 100.50),
        (116, 12, 60, 120.75)
    ]
    cursor.executemany('INSERT INTO staff_work_hours (Staff_ID, Num_Events, Num_Hours, Travel_Fees) VALUES (?, ?, ?, ?);', work_hours)
    
    print('Inserting data into inventory_data table')
    inventory_data = [
        (1, 'Balloons', 'Clown Costume', 50),
        (2, 'Plates', 'Princess Costume', 100),
        (3, 'Cups', 'Superhero Costume', 80),
        (4, 'Napkins', 'Pirate Costume', 60),
        (5, 'Candles', 'Magician Costume', 40),
        (6, 'Party Hats', 'Fairy Costume', 70),
        (7, 'Streamers', 'Animal Costume', 90),
        (8, 'Banners', 'Space Suit', 110),
        (9, 'Confetti', 'Astronaut Costume', 75),
        (10, 'Ribbons', 'Dinosaur Costume', 55),
        (11, 'Party Favors', 'Knight Costume', 95),
        (12, 'Gift Bags', 'Pirate Costume', 65),
        (13, 'Tablecloths', 'Wizard Costume', 85),
        (14, 'Centerpieces', 'Ninja Costume', 70),
        (15, 'Invitations', 'Superhero Costume', 120),
        (16, 'Thank You Cards', 'Princess Costume', 100)
    ]
    cursor.executemany('INSERT INTO inventory_data (Inventory_ID, Supplies, Costume_Inventory, Quantities) VALUES (?, ?, ?, ?);', inventory_data)
    
    print('Inserting data into inventory_needed table')
    inventory_needed = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16)
    ]
    cursor.executemany('INSERT INTO inventory_needed (Inventory_ID, Party_ID) VALUES (?, ?);', inventory_needed)

    conn.commit()
    cursor.close()
    conn.close()
    print('Data inserted into database')

insert_sample_data("party_kids_remember.db")
