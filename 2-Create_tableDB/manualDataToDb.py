import sqlite3
result=[
    # (1, '011-0476', 'IQ8712NE-V18', 'A14'),
    # (2, '011-0487', 'IQD62NI-B7', 'A11'),
    # (3, '011-0490', 'IQD61WV-F13', 'D02')
]
# Connect to the database (creates a new file if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the 'products' table
create_table_query = '''
CREATE TABLE `users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT,
  `status` TEXT,
  `date` DATE
);
'''
cursor.execute(create_table_query)

# Insert values into the 'products' table
# Values to be inserted


# Insert values into the 'products' table
insert_query = '''
    INSERT INTO users (`id`, `name`, `status`, `date`)
    VALUES (?, ?, ?, ?)
'''

cursor.executemany(insert_query, result)




# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and values inserted successfully.")
