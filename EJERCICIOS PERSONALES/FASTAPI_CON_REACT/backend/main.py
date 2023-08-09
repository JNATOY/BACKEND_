from fastapi import FastAPI

app = FastAPI()

@app.get ('/')
def root():
    return ' Hi , mi name es FastAPI'