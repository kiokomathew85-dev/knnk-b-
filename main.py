import sqlite3
import pandas as pd

# ==========================================
# PART 1: Connecting to the Data
# ==========================================

# STEP 1A & 1B
# Import SQL Library, Pandas, and connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference code provided by the lab to see employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# ==========================================
# PART 2: Basic Select Filtering
# ==========================================

# STEP 2
# Select employee number and last name from all employees
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# STEP 3
# Select last name and employee number (reversed column order)
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)


# ==========================================
# PART 3: Aliasing in Select
# ==========================================

# STEP 4
# Select last name and rename employee number column to 'ID'
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)


# ==========================================
# PART 4: CASE Function
# ==========================================

# STEP 5
# Categorize executive roles and output a new column called 'role'
df_executive = pd.read_sql("""
    SELECT *,
        CASE 
            WHEN jobTitle = 'President' 
              OR jobTitle = 'VP Sales' 
              OR jobTitle = 'VP Marketing' THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)


# ==========================================
# PART 5: Built-In Functions - Strings
# ==========================================

# STEP 6
# Find the character length of the last name as 'name_length'
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""", conn)

# STEP 7
# Extract the first two characters of each job title as 'short_title'
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)


# ==========================================
# PART 6: Built-In Functions - Numerics & Dates
# ==========================================

# Reference code provided by the lab to see order details
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Select the internal rounded product of each row, then apply pandas .sum()
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price 
    FROM orderDetails
""", conn).sum()

# STEP 9
# Select original order date alongside parsed day, month, and year fields
df_day_month_year = pd.read_sql("""
    SELECT 
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders
""", conn)


# ==========================================
# Close Connection
# ==========================================
conn.close()
