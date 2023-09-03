from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    with open('log.txt', 'a') as f:
        f.write(str(datetime.now()))
    return b"Hello to Ronan's FastAPI Deployment"
