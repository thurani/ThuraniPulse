from fastapi import FastAPI, HTTPException, Depends, Form
from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "thuraniprofiledb"
)

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

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/get_users")
def get_users():
    cursor = conn.cursor(dictionary = True)
    cursor.execute("select * from users")
    records = cursor.fetchall()
    return records
