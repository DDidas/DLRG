import sqlite3
import datetime
import eel

# Initialize Eel with the folder containing your web files
eel.init('../frontend/', allowed_extensions=[".html", ".js", ".css", ".woff", ".svg", ".svgz", ".png"])

options = {
    'mode': "kiosk",  # Use "kiosk" for fullscreen
    'host': 'localhost',
    'port': 8080
}


@eel.expose  # Expose this function to JavaScript
def activate_pin_20():
    # GPIO.output(20, GPIO.HIGH)
    return {"message": "Pin 20 activated successfully"}


@eel.expose
def deactivate_pin_20():
    # GPIO.output(20, GPIO.LOW)
    return {"message": "Pin 20 deactivated successfully"}


@eel.expose
def create_user(user_data):
    conn = sqlite3.connect("../identifier.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.accounts VALUES (?,?,?,?)", (
        user_data['id'], user_data['name'], 0, user_data['admin']
    ))
    conn.commit()
    cursor.close()
    return {"message": f"User {user_data['name']} created successfully"}


@eel.expose
def update_guthaben(user_data):
    conn = sqlite3.connect("../identifier.sqlite")
    cursor = conn.cursor()
    cursor.execute("UPDATE main.accounts SET guthaben = ? WHERE id = ?", (user_data['neues_guthaben'], user_data['id']))
    conn.commit()
    cursor.close()
    return {"message": f"Guthaben of user with ID {user_data['id']} updated successfully"}


@eel.expose
def check_if_user_exists(id):
    conn = sqlite3.connect("../identifier.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts WHERE id = ?)", (id,))
    result = cursor.fetchone()[0]
    conn.close()
    return {"exists": bool(result)}


@eel.expose
def get_adminstatus_by_id(id):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT admin FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"admin": str(result[0])} if result else {"admin": None}


@eel.expose
def get_name_by_id(id):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"name": str(result[0])} if result else {"name": None}


@eel.expose
def get_guthaben_by_id(id):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT guthaben FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"guthaben": float(result[0])} if result else {"guthaben": None}


@eel.expose
def export_users_csv():
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name, guthaben FROM accounts")
    results = cursor.fetchall()
    conn.close()

    csv_content = "Name,Rechnung\n" + "\n".join([f"{name},{guthaben}" for name, guthaben in results])
    return csv_content


@eel.expose
def reset_guthaben():
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()

    today = datetime.datetime.today()
    table_name = "abrechnung_" + today.strftime('%Y%m%d_%H%M%S')  # use only digits and underscore
    cursor.execute(f"CREATE TABLE {table_name} AS SELECT * FROM main.accounts")

    cursor.execute("UPDATE main.accounts SET guthaben = 0")

    conn.commit()
    cursor.close()
    return {"message": f"Guthaben reset and table {table_name} created successfully"}


@eel.expose
def get_logbuch_entries():
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, date FROM logbuch")
    results = cursor.fetchall()
    conn.close()

    return results


@eel.expose
def log_action(action_data):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO logbuch (name, price, date) VALUES (?, ?, ?)",
                   (action_data['name'], action_data['action'], timestamp))

    conn.commit()
    cursor.close()
    return {"message": f"Action logged successfully"}


eel.init('../frontend/', allowed_extensions=[".html", ".js", ".css", ".woff", ".svg", ".svgz", ".png"])

# Start Eel with the main HTML file
eel.start('html/login_eel.html', port=8080, mode='chrome', cmdline_args=['--kiosk'])
