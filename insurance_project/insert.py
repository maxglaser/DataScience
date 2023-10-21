import csv
import psycopg2

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="your_user",
        password="your_password"
    )
except Exception as e:
    print(f"Error: {e}")
    exit()

# Create a cursor object
cursor = conn.cursor()

# Create the table (only if it doesn't exist)
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS health_data (
        id SERIAL PRIMARY KEY,
        age INTEGER,
        sex VARCHAR(10),
        bmi REAL,
        children INTEGER,
        smoker VARCHAR(10),
        region VARCHAR(20),
        charges REAL
    );
    """)
except Exception as e:
    print(f"Error: {e}")

# Commit the transaction
conn.commit()

# Read data from CSV file and insert into the table
try:
    with open('insurance.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            cursor.execute("""
            INSERT INTO health_data (age, sex, bmi, children, smoker, region, charges)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
except Exception as e:
    print(f"Error: {e}")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
