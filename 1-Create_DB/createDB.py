import sqlite3

# Creates a new file if it doesn't exist
conn = sqlite3.connect('users.db')
cursor = conn.cursor()




# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and values inserted successfully.")
