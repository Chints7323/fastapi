from fastapi import FastAPI
from db import get

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello world"}

app.get("/get_data")
def get_path():
    return {"message":"route"}
