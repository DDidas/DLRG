from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3

from fastapi.middleware.cors import CORSMiddleware

# import RPi.GPIO as GPIO

# set up the GPIO pin
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(20, GPIO.OUT)

app = FastAPI()

# Add middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
        user_data['id'], user_data['name'], user_data['guthaben'], user_data['admin']
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
