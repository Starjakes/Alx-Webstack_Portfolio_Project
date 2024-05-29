import mysql.connector

# Establish connection to MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Adejo4gud'
)

# Create cursor object to execute SQL queries
my_cursor = mydb.cursor()

# Execute CREATE DATABASE statement
my_cursor.execute("CREATE DATABASE IF NOT EXISTS jayhlens")

# Commit the changes
mydb.commit()

# Reconnect to MySQL to ensure the created database is selected
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Adejo4gud',
    database='jayhlens'  # Select the created database
)

# Create a new cursor object
my_cursor = mydb.cursor()

# Execute CREATE TABLE statement for admin table
create_admin_table_sql = """
CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""

# Execute the SQL statement to create the admin table
my_cursor.execute(create_admin_table_sql)

# Commit the changes
mydb.commit()

# Execute SHOW TABLES statement to verify the creation of tables
my_cursor.execute("SHOW TABLES")

# Fetch and print the result
for table in my_cursor:
    print(table)
