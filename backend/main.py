from fastapi import FastAPI, HTTPException, Depends, Form
from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

def get_db_connection():
    """Function to create a MySQL connection."""
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "thuraniprofiledb"
        )
        return conn
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class UserCreate(BaseModel):
    name: str
    title: str
    summary: str
    emailaddress: str
    location: str

class CreateSkill(BaseModel):
    user_id: int
    skill_name: str

class UserHobby(BaseModel):
    user_id: int
    hobby_name: str
    description: str

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/get_users/")
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary = True)
        cursor.execute("select * from users")
        records = cursor.fetchall()
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/get_skills/")
def get_skills():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary = True)
        cursor.execute("select * from skills")
        records = cursor.fetchall()
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/get_hobbies/")
def get_hobbies():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary = True)
        cursor.execute("select * from hobbies")
        records = cursor.fetchall()
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
