import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3
import csv
from fastapi.responses import FileResponse

from fastapi.middleware.cors import CORSMiddleware

# import RPi.GPIO as GPIO

# set up the GPIO pin
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(20, GPIO.OUT)

app = FastAPI()

# Add middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "/Users/daviddidas/Desktop/DLRG_KOMPRESSOR/frontend/html"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/activate_pin_20")
async def activate_pin_20_endpoint():
    # GPIO.output(20, GPIO.HIGH)
    return {"message": "Pin 20 activated successfully"}


@app.post("/deactivate_pin_20")
async def deactivate_pin_20_endpoint():
    # GPIO.output(20, GPIO.LOW)
    return {"message": "Pin 20 deactivated successfully"}


@app.post("/create_user")
async def create_user_endpoint(user_data: dict):
    conn = sqlite3.connect("../identifier.sqlite")
    zeiger = conn.cursor()
    zeiger.execute("INSERT INTO main.accounts VALUES (?,?,?,?)", (
        user_data['id'], user_data['name'], 0, user_data['admin']
    ))
    conn.commit()
    zeiger.close()
    return {"message": f"User {user_data['name']} created successfully"}


@app.put("/update_guthaben")
async def update_guthaben_endpoint(user_data: dict):
    conn = sqlite3.connect("../identifier.sqlite")
    zeiger = conn.cursor()
    zeiger.execute("UPDATE main.accounts SET guthaben = ? WHERE id = ?", (user_data['neues_guthaben'], user_data['id']))
    conn.commit()
    zeiger.close()
    return {"message": f"Guthaben of user with ID {id} updated successfully"}


@app.get("/check_if_user_exists")
async def check_if_user_exists_endpoint(id: int):
    conn = sqlite3.connect("../identifier.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts WHERE id = ?)", (id,))
    result = cursor.fetchone()[0]
    conn.close()
    return {"exists": bool(result)}


@app.get("/get_adminstatus_by_id")
async def get_name_by_id_endpoint(id: int):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT admin FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"admin": str(result[0])} if result else {"admin": None}


@app.get("/get_name_by_id")
async def get_name_by_id_endpoint(id: int):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"name": str(result[0])} if result else {"name": None}


@app.get("/get_guthaben_by_id")
async def get_guthaben_by_id_endpoint(id: int):
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT guthaben FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"guthaben": float(result[0])} if result else {"guthaben": None}


import csv
from fastapi.responses import FileResponse


@app.get("/export_users_csv")
async def export_users_csv_endpoint():
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name, guthaben FROM accounts")
    results = cursor.fetchall()
    conn.close()

    # Create a temporary file to store the CSV data
    filename = "users.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Guthaben"])  # Write header
        writer.writerows(results)  # Write user data rows

    # Return the CSV file as a download
    return FileResponse(filename, filename="users.csv", media_type='text/csv')


@app.get("/reset_guthaben")
async def reset_guthaben_endpoint():
    conn = sqlite3.connect('../identifier.sqlite')
    cursor = conn.cursor()

    # Create a new table with the name "abrechnung_" + current date
    today = datetime.datetime.today()
    table_name = "abrechnung_" + today.strftime("%Y%m%d%H%M%S")
    cursor.execute(f"CREATE TABLE {table_name} AS SELECT * FROM main.accounts")

    # Set guthaben of all users to 0
    cursor.execute("UPDATE main.accounts SET guthaben = 0")

    conn.commit()
    conn.close()
    return {"message": f"Guthaben reset and table {table_name} created successfully"}