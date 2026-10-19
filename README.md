### INF601 - Advanced Programming in Python
### Rachel White
### Mini Project 5
 
 
# Reading Log
 
Reading Log is a Flask web app for keeping track of the books you read, with user accounts, a SQLite database, and Bootstrap styling.
 
## Description
 
Reading Log lets users register, log in, and add books to a shared reading log. Each book has a title, author, reading status (Want to read, Reading, or Finished), an optional 1-5 rating, and notes. All books are listed on the home page as Bootstrap cards, with colored badges for status and rating. Users can only edit or delete the books they added themselves, and a Bootstrap modal asks for confirmation before a book is deleted.

The project follows the structure of the official [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/), with the blog posts changed into books.

 
## Getting Started
 
### Dependencies
 
* Python 3 (developed with Python 3.14 on Windows 11)
* Flask, which is listed in `requirements.txt`. Its dependencies (Werkzeug, Jinja2, Click, etc.) install automatically.
* An internet connection, because Bootstrap 5.3 is loaded from the jsDelivr CDN.
* Install the requirements with:
```
pip install -r requirements.txt
```
 
### Installing
 
* https://github.com/rachelr801/miniproject5RachelWhite.git
 
### Executing program
 
* Create a virtual environment:
```
python -m venv .venv
```
* Activate it on Windows (PowerShell):
```
.venv\Scripts\Activate.ps1
```
* Or activate it on macOS or Linux:
```
source .venv/bin/activate
```
* Install the requirements:
```
pip install -r requirements.txt
```
* Initialize the database. Run this once before starting the app for the first time. It creates `instance/flaskr.sqlite`.
```
flask --app flaskr init-db
```
* With the virtual environment activated, start the development server:
```
flask --app flaskr run --debug
```
* Open http://127.0.0.1:5000 in your browser.
* Click **Register** and create an account.
* Log in with that account.
* Click **+ Add Book**, fill out the form, and click **Save**.
* Click **Edit** on one of your books to change it, or click **Delete** and confirm in the popup to remove it.
 
## Help
 
* **`no such table: books`**: the database hasn't been created yet, or it was made with an older schema. Run `flask --app flaskr init-db`. This erases all existing users and books.
* **`flask` is not recognized**: the virtual environment isn't activated. Activate it, or run `.venv\Scripts\flask.exe` directly.
* **PowerShell won't run `Activate.ps1`**: run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.
* **Pages look unstyled or the Delete popup won't open**: Bootstrap couldn't load from the CDN, so check your internet connection.
* To see Flask's built-in help for any command:
```
flask --app flaskr --help
```
 
## Authors
 
Rachel White
  
## Version History
 
* 0.1
    * Initial Release
 
## License
 
This project was created as coursework for INF601 and is not licensed for reuse
 
## Acknowledgments

* [Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)

## AI Usage

I wrote most of the code myself by following the Flask tutorial. I converted the tutorial blog into a reading log and asked Claude to check the schema.sql, books.py, and templates to ensure that I caught all of the changes necessary to conver the blog to a reading log. As Claude found syntax issues and bugs, I reviewed the suggestions and corrected the code. This was especially helpful for findings queries that still used the 'post' table. I tested the app myself and also had Claude test it against the project rubric.
