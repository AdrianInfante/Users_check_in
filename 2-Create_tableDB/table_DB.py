import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS nameyourtablehere(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
                
            )
        ''')

cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)')

conn.commit()
conn.close()

print("Database created and values inserted successfully.")
