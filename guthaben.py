#!/usr/bin/env python3

import cgi
import cgitb
import mysql.connector

cgitb.enable()

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Formulardaten lesen
form = cgi.FieldStorage()
userid = form.getvalue("userid")
amount = float(form.getvalue("amount"))

# Guthaben des Benutzers aktualisieren
mycursor = mydb.cursor()
mycursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, userid))
mydb.commit()

# Bestätigungsnachricht anzeigen
print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>Balance Added</title>")
print("</head>")
print("<body>")
print("<h2>Balance Added</h2>")
print("<p>The balance of user with ID " + str(userid) + " has been updated.</p>")
print("<p>New balance: " + str(amount) + " euros</p>")
print("<a href='/login.html'>Go back to login page</a>")
print("</body>")
print("</html>")
