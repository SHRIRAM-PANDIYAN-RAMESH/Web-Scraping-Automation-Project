#-----------------------------------------------
# Database Connection
#-----------------------------------------------

import mysql.connector as conn  # Here we import mysql.connector module under the name "conn", just for our normal and easy variable use

def get_connection(): # Here, we define a function named get_connection() which uses the connect() method to connect to the SQL Server and Database by providing details of host, username, password, port and database name
    connection = conn.connect(
        host="localhost",
        user="root",
        password="351975",
        port=3307,
        database="ecommerce_tracker",
        charset="utf8mb4"
    )
    return connection  # Then we return the connection which we established inside the function.
