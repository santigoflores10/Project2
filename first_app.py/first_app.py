import sqlite3
import scripts.create_database as create_db  
import scripts.insert_data as db_insert      
from bottle import route, run, template, static_file, request, redirect
#connect database
CONN = sqlite3.connect('party_kids_remember.db')
CONN.row_factory = sqlite3.Row
CURSOR = CONN.cursor()
#create database 
@route('/create_database')
def create_database():
    create_db.create_empty_database('party_kids_remember.db')
    return template('database_create')
#insert data
@route('/insert_data')
def insert_data():
    db_insert.insert_sample_data('party_kids_remember.db')
    return template('database_insert')

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')
#run indext tpl
@route('/')
def index():
    return template('index')
#select all customers names
@route('/customers')
def customers():
    query = 'SELECT First_name, Last_name FROM customer_personal_details'
    CURSOR.execute(query)
    customer_list = CURSOR.fetchall()
    return template('customers', customers=customer_list)

@route('/static_all_parties')
def select_all_parties():
    query = 'SELECT * FROM customer_party_details'
    CURSOR.execute(query)
    result = CURSOR.fetchall()
    return template('results', records=result, title='All Parties')
#count amount of customers
@route('/count_customers')
def count_customers():
    query = 'SELECT COUNT(*) as total_customers FROM customer_personal_details'
    CURSOR.execute(query)
    result = CURSOR.fetchone()
    return template('results', records=[result], title='Total Customers')
#add up payments
@route('/sum_payments')
def sum_payments():
    query = 'SELECT SUM(Payments) as total_payments FROM customer_financial_records'
    CURSOR.execute(query)
    result = CURSOR.fetchone()
    return template('results', records=[result], title='Total Payments')
#average out age of children
@route('/average_age')
def average_age():
    query = 'SELECT AVG(Age_Turning) as average_age FROM customer_party_details'
    CURSOR.execute(query)
    result = CURSOR.fetchone()
    return template('results', records=[result], title='Average Age of Children')
#find min and max quantity
@route('/min_max_inventory')
def min_max_inventory():
    query = '''
    SELECT 
        MIN(Quantities) as min_quantity, 
        MAX(Quantities) as max_quantity 
    FROM inventory_data
    '''
    CURSOR.execute(query)
    result = CURSOR.fetchone()
    return template('results', records=[result], title='Min and Max Inventory Quantities')
# output all supplies
@route('/grouped_inventory')
def grouped_inventory():
    query = '''
    SELECT Supplies, SUM(Quantities) as total_quantity
    FROM inventory_data
    GROUP BY Supplies
    ORDER BY total_quantity DESC
    '''
    CURSOR.execute(query)
    result = CURSOR.fetchall()
    return template('results', records=result, title='Total Inventory by Supplies')
#output all details regarding customer party details
@route('/customer_party_join')
def customer_party_join():
    query = '''
    SELECT Party_ID, Party_Theme, Child_name, Age_Turning, Number_children_Attending, 
           Booking_ID, Inventory_ID, Staff_ID, 
           Character_Requested, Inventory_ID, 
           Booking_ID, Party_ID, First_name, Last_name 
    FROM customer_party_details 
    JOIN customer_personal_details 
    ON Booking_ID = Customer_ID
    '''
    CURSOR.execute(query)
    result = CURSOR.fetchall()
    return template('results', records=result, title='Customer Party Details with Customer Information')

@route('/static_all_inventory')
def select_all_inventory():
    query = 'SELECT * FROM inventory_data'
    CURSOR.execute(query)
    result = CURSOR.fetchall()
    return template('results', records=result, title='All Inventory')

# Route to update a customer
@route('/update_customer/<customer_id:int>', method='POST')
def update_customer(customer_id):
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    phone_number = request.forms.get('phone_number')

    
    update_query = f'''
    UPDATE customer_personal_details
    SET First_name = '{first_name}', Last_name = '{last_name}', Phone_number = '{phone_number}'
    WHERE Customer_ID = {customer_id};
    '''
    
    CURSOR.execute(update_query)
    CONN.commit()
    return redirect('/customers')

# Route to delete a customer
@route('/delete_customer/<customer_id:int>')
def delete_customer(customer_id):
    delete_query = f'''
    DELETE FROM customer_personal_details
    WHERE Customer_ID = {customer_id};
    '''
    
    CURSOR.execute(delete_query)
    CONN.commit()
    return redirect('/customers')

run(host='localhost', port=8080, debug=True, reloader=True)
CURSOR.close()
CONN.close()
