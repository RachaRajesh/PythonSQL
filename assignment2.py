import sqlite3

try:
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
        emp_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        birth_date DATE,
        sex VARCHAR(1),
        salary INTEGER,
        super_id INTEGER,
        branch_id INTEGER
    )''')

    cursor.execute('''INSERT OR IGNORE INTO Employee VALUES(100,'david','Wallace','1967-11-17','M',250000,3,1)''')

    cursor.execute("INSERT OR IGNORE INTO Employee (emp_id, sex) VALUES (?, ?)", (120, 'F'))


    connection.execute("UPDATE Employee SET last_name = 'Change' WHERE salary = 250000")


    cursor.execute('''SELECT * FROM Employee''')
    rows = cursor.fetchall()
    for row in rows:
        print("Updated data is:", row)


    cursor.execute("SELECT * FROM nonTABLE")

except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")
    connection.rollback()

finally:
    connection.commit()
    connection.close()
