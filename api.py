from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create_user")
async def create_user_endpoint(id: int, name: str, guthaben: float):
    conn = sqlite3.connect("identifier.sqlite")
    zeiger = conn.cursor()
    zeiger.execute("INSERT INTO main.accounts VALUES (?,?,?)", (id, name, guthaben,))
    conn.commit()
    zeiger.close()
    return {"message": f"User {name} created successfully"}


@app.put("/update_guthaben")
async def update_guthaben_endpoint(id: int, neues_guthaben: float):
    conn = sqlite3.connect("identifier.sqlite")
    zeiger = conn.cursor()
    zeiger.execute("UPDATE main.accounts SET guthaben = ? WHERE id = ?", (neues_guthaben, id))
    conn.commit()
    zeiger.close()
    return {"message": f"Guthaben of user with ID {id} updated successfully"}


@app.get("/check_if_user_exists")
async def check_if_user_exists_endpoint(id: int):
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts WHERE id = ?)", (id,))
    result = cursor.fetchone()[0]
    conn.close()
    return {"exists": bool(result)}


@app.get("/get_name_by_id")
async def get_name_by_id_endpoint(id: int):
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"name": str(result[0])} if result else {"name": None}


@app.get("/get_guthaben_by_id")
async def get_guthaben_by_id_endpoint(id: int):
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT guthaben FROM accounts WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return {"guthaben": float(result[0])} if result else {"guthaben": None}