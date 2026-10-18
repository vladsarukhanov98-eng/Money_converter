import os

from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI(title="Конвертер рублей")
load_dotenv()


@app.get("/")
def root():
    return {"Message": "Сервис работает"}


@app.get("/health")
def health():
    return {"Status": "OK"}


@app.get("/rates")
def get_rates():
    return {"USD": 84.9, "EUR": 94.97, "CNY": 12.67}


@app.get("/place")
def place(name: str = "Остальной Мир"):
    name = name.title()
    if name == "Китай":
        valute = "CNY"
    elif name == "Европа":
        valute = "EUR"
    else:
        valute = "USD"
    return {"Регион": name, "Валюта": valute}


@app.get("/convert")
def convert(rub: float = 0, region: str = "Остальной Мир"):
    region = region.title()
    if region == "Китай":
        return {"Юани": round(rub / 12.67, 2)}
    elif region == "Европа":
        return {"Евро": round(rub / 94.97, 2)}
    else:
        return {"Доллары": round(rub / 84.9, 2)}


@app.get("/version")
def version():
    return {"Version": "0.1.0"}


@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "Учебный сервис")
    app_author = os.getenv("APP_AUTHOR", "Не указан")
    return {"App Name": app_name, "Author": app_author}