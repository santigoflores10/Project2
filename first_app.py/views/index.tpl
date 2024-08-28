<!DOCTYPE html>
<html>
    <head>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
        <title>Parties Kids Remember</title>
    </head>
    <body>
        <h1>Welcome to Parties Kids Remember!</h1>

        <p><a href="/customers">View All Customers</a></p>
        <p><a href="/static_all_parties">View All Party Details</a></p>
        <p><a href="/static_all_inventory">View All Inventory</a></p>
        <p><a href="/count_customers">Total Number of Customers</a></p>
        <p><a href="/sum_payments">Total Payments Made by Customers</a></p>
        <p><a href="/average_age">Average Age of Children at Parties</a></p>
        <p><a href="/min_max_inventory">Min and Max Inventory Quantities</a></p>
        <p><a href="/grouped_inventory">Total Inventory Grouped by Supplies</a></p>
        <p><a href="/customer_party_join">View Detailed Party Info with Customer Names</a></p>

        <div class="container">
            <h2>Database Management</h2>
        
            
            <form action="/insert_customer" method="post">
                <label for="first_name">First Name:</label><br>
                <input type="text" id="first_name" name="first_name" required><br><br>
        
                <label for="last_name">Last Name:</label><br>
                <input type="text" id="last_name" name="last_name" required><br><br>
        
                <label for="phone_number">Phone Number:</label><br>
                <input type="text" id="phone_number" name="phone_number" required><br><br>
        
                <label for="address">Address:</label><br>
                <input type="text" id="address" name="address" required><br><br>
        
                <input type="submit" value="Insert Customer Data">
            </form>
        
            
            <form action="/delete_customer" method="post">
                <label for="customer_id">Customer ID to Delete:</label><br>
                <input type="text" id="customer_id" name="customer_id" required><br><br>
        
                <input type="submit" value="Delete Customer Data">
            </form>
        </div>
        