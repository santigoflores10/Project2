<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Management</title>
</head>
<body>
    <h1>Customer Management</h1>

    <h2>Customer List</h2>
    <ul>
        % for customer in customers:
            <li>
                {{customer['First_name']}} {{customer['Last_name']}} - {{customer['Phone_number']}}
                
                
                <form action="/update_customer/{{customer['Customer_ID']}}" method="post" style="display:inline;">
                    <input type="text" name="first_name" value="{{customer['First_name']}}" required>
                    <input type="text" name="last_name" value="{{customer['Last_name']}}" required>
                    <input type="text" name="phone_number" value="{{customer['Phone_number']}}" required>
                    <button type="submit">Update</button>
                </form>

            
                <a href="/delete_customer/{{customer['Customer_ID']}}" onclick="return confirm('Are you sure you want to delete this customer?');">Delete</a>
            </li>
        % end
    </ul>
</body>
</html>
