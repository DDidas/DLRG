#!/usr/bin/python
import cgi
import mysql.connector

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Daten aus dem Formular lesen
form = cgi.FieldStorage()
userid = form.getvalue("userid")
password = form.getvalue("password")

# Überprüfen, ob der Benutzer in der Datenbank vorhanden ist
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users WHERE id = %s AND password = %s", (userid, password))
result = mycursor.fetchone()

# Wenn der Benutzer gefunden wurde, den Namen und das Guthaben anzeigen
if result:
    name = result[1]
    balance = result[2]
    print("Content-type: text/html\n\n")
    print("<html>")
    print("<head>")
    print("<title>Login Successful</title>")
    print("</head>")
    print("<body>")
    print("<h2>Welcome, " + name + "!</h2>")
    print("<p>Your balance is: " + str(balance) + " EUR</p>")
    print("<form action='update_balance.py' method='post'>")
    print("<label for='amount'>Enter amount to deduct:</label>")
    print("<input type='number' step='0.01' id='amount' name='amount'><br><br>")
    print("<input type='submit' value='Submit'>")
    print("</form>")
    print("<br>")
    print("<form action='add_balance.py' method='post'>")
    print("<label for='adminpassword'>Admin password:</label>")
    print("<input type='password' id='adminpassword' name='adminpassword'><br><br>")
    print("<label for='amount'>Enter amount to add:</label>")
    print("<input type='number' step='0.01' id='amount' name='amount'><br><br>")
    print("<input type='submit' value='Add Balance'>")
    print("</form>")
    print("<br>")
    print("<form action='logout.py' method='post'>")
    print("<input type='submit' value='Logout'>")
    print("</form>")
    print("</body>")
    print("</html>")
else:
    print("Content-type: text/html\n\n")
    print("<html>")
    print("<head>")
    print("<title>Login Failed</title>")
    print("</head>")
    print("<body>")
    print("<h2>Login Failed</h2>")
    print("</body>")
    print("</html>")