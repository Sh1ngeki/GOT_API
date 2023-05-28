# GOT_API
## API Request
- Import the requests library to make HTTP requests.
- Use the requests.get() method to retrieve data from the 'https://thronesapi.com/api/v2/Characters' endpoint.
- Store the response content as JSON using response.json().
## JSON Data Handling
- The JSON data obtained from the API response is stored in the content variable.
- (Optional) Save the JSON data to a file using the json.dump() method.
## SQLite Database Operations
- Import the sqlite3 library to work with SQLite databases.
- Create a SQLite database file named 'GOT.sqlite' (if it doesn't exist) using the sqlite3.connect() method.
- Create a table named 'GOT' with specific columns if it doesn't exist using the cur.execute() method.
- Insert data from the API response into the 'GOT' table using a loop and the cur.execute() method.
- Commit the changes to the database using conn.commit() and close the connection using conn.close().
## Notification Display
- Import the win10toast library to display notifications on Windows 10.
- Define a notify() function to display notifications.
- The notify() function makes a new API request to retrieve data and randomly selects a character's name.
- Display the notification using the win10toast.ToastNotifier().show_toast() method.
- Use the schedule library to run the notify() function every 10 seconds.
- Run the scheduled tasks using schedule.run_pending() and pause execution for 1 second using time.sleep().

![Ghost Will Return in 'Game of Thrones' Season 8 and We Can't Wait](https://github.com/Sh1ngeki/GOT_API/assets/115181439/184ad44c-e5dc-4925-abe4-54b5d94881ca)
