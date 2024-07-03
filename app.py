from flask import Flask, render_template, request, jsonify,request
import sqlite3
import time
import pandas as pd
from datetime import date as today_date
import schedule
import threading
import requests

app = Flask(__name__)

db = './users.db'


@app.route('/')
def checkin():
    return render_template('index.html')

# Dictionary mapping user names to their Notion page IDs
user_notion_ids = {
    'adrian': 'a2fb642368c446efba04c59afb583c18',
    
}


@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    name = data.get('name')
    status = data.get('status')
    date = data.get('date') 

    # Insert the data into the database, including the date
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, status, date) VALUES (?, ?, ?)", (name, status, date))
    conn.commit()
    conn.close()

    # If the user's Notion page ID is available, update their status on Notion
    if name.lower() in user_notion_ids:
        update_user_notion_status(name.lower(), status)

    return jsonify(message='Status updated successfully')

@app.route('/delete_status', methods=['DELETE'])
def delete_status():
    data = request.get_json()
    name = data.get('name')

    # Delete the status from the database
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()
    conn.close()

    return jsonify(message='Status deleted successfully')


def update_user_notion_status(name, status):
    
    notion_id = user_notion_ids.get(name)
    if notion_id:
        url = f"https://api.notion.com/v1/pages/{notion_id}"
        payload = {
            "properties": {
                "Status": {
                    "select": {
                        "name": status
                    }
                }
            }
        }
        headers = {
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28',
            'Authorization': 'Bearer ', #Here goes the Internal Integration Secret from your notion integration portal
            
        }
        response = requests.patch(url, headers=headers, json=payload)
        if response.ok:
            print(f"{name.capitalize()}'s status updated on Notion: {status}")
        else:
            print(f"Failed to update {name.capitalize()}'s status on Notion.")
    else:
        print(f"No Notion ID found for {name.capitalize()}.")

    return response.text


@app.route('/get_user_statuses', methods=['GET'])
def get_user_statuses():
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    
    user_statuses = {}
    
    today = today_date.today().strftime('%Y-%m-%d')
    
    # Retrieve the status and date for each user from the database
    names = ['adrian','alison', 'amy]
    
    for name in names:
        cursor.execute("SELECT status, date FROM users WHERE name = ? AND date(date) = ?", (name, today))
        result = cursor.fetchone()
        if result:
            status, date = result
            user_statuses[name] = {'status': status, 'date': date}
    
    connection.close()
    
    return jsonify(user_statuses)

@app.route('/checkin_list')
def retrieve_data():
    try:

        conn = sqlite3.connect(db)
        cursor = conn.cursor()


        cursor.execute('SELECT id, name, status, date FROM users')


        data = cursor.fetchall()

        conn.close()


        return render_template('checkin_list.html', data=data)

    except sqlite3.Error as e:
        print('SQLite Error:', e)
        return 'An error occurred while retrieving data.'


 
def update_notion(status):
    for name in user_notion_ids:
        update_user_notion_status(name, status)

def scheduled_job():
    # Call update_status with sample data
    update_notion('No Status')

# Schedule the job
schedule.every().day.at("23:59").do(scheduled_job)

def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # Start the scheduling loop in a separate thread
    scheduling_thread = threading.Thread(target=run_scheduled_tasks)
    scheduling_thread.start()

    # Run the Flask app in the main thread
    app.run(host='10.253.0.95', port=5000, debug=True)






