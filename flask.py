import sqlite3

def check_if_user_exists(id):
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts WHERE id = ?)", (id,))
    result = cursor.fetchone()[0]
    conn.close()
    return bool(result)

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Check User</title>")
print("</head>")
print("<body>")
print("<h1>Check User</h1>")
print("<form method='post'>")
print("<label for='user_id'>User ID:</label>")
print("<input type='text' id='user_id' name='user_id'><br><br>")
print("<input type='submit' value='Check User'>")
print("</form>")

if "user_id" in form:
    user_id = form.getvalue("user_id")
    if check_if_user_exists(user_id):
        print("<p>User exists.</p>")
    else:
        print("<p>User does not exist.</p>")

print("</body>")
print("</html>")
