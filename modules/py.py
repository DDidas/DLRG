
import sqlite3


def create_user(id, name, guthaben):
    conn = sqlite3.connect("../identifier.sqlite")
    zeiger = conn.cursor()
    zeiger.execute("INSERT INTO main.accounts VALUES (?,?,?)", (id, name, guthaben,))
    conn.commit()
    zeiger.close()


def update_guthaben(id, neues_guthaben):
    conn = sqlite3.connect("../identifier.sqlite")
    zeiger = conn.cursor()
    zeiger.execute("UPDATE main.accounts SET guthaben = ? WHERE id = ?", (neues_guthaben, id))
    conn.commit()
    zeiger.close()


def check_if_user_exists(id):
    conn = sqlite3.connect("../identifier.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts WHERE id = ?)", (id,))
    result = cursor.fetchone()[0]
    conn.close()
    return bool(result)

def get_name_by_id(id):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return str(result[0]) if result else None

def get_guthaben_by_id(id):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT guthaben FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return float(result[0]) if result else None


if __name__ == "__main__":
    id = 3
    name = "NAME DER r32t"
    haben = 43.50
    if not check_if_user_exists(id):
        create_user(id, name, haben)
    print(get_guthaben_by_id(id))
