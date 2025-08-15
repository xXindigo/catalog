from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Добро пожаловать в каталог книг и фильмов!"}