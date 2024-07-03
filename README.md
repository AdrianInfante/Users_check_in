
# Flask Application with Notion Integration

This repository contains a Flask web application that integrates with an SQLite database for managing product information and user statuses. It includes functionality for uploading data from Excel files, updating and deleting user statuses, and scheduling tasks for automating processes.

## Features

- **Upload Excel Data**: Allows users to upload Excel files containing product information, which are then stored in an SQLite database (`users.db`).
- **Update Status**: Users can update their status with a date stamp records.
- **Integration with Notion**: Updates user status on Notion based on a predefined mapping of user names to Notion page IDs.
- **Scheduled Tasks**: Includes scheduled tasks using the `schedule` library:
  - Updates Notion status for all users to 'No Status' daily, to refresh the status, in this example would be at 23:59.

## Project Structure

- **`app.py`**: Main Flask application script containing route definitions and database operations.
- **`users.db`**: SQLite database file storing product information and user check-in statuses.
- **`templates/`**: Directory containing HTML templates for rendering web pages (`index.html`, `checkin_list.html`).

## Requirements

Ensure you have Python 3.x installed along with the necessary libraries listed in `requirements.txt`. Install dependencies using:

```
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Set up a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Start the Flask application:

   ```
   python app.py
   ```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

- **Update Status**: Send a POST request to `/update_status` with JSON payload containing `name`, `status`, `date` to update user status.
- **View Check-in List**: Navigate to `/checkin_list` to view all user check-in records.

## Generate token for Notion
    https://www.notion.so/profile/integrations 

## Where to obtain the user page ID





## Future updates

- Customize error handling and logging.

