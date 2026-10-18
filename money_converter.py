import os
import logging
from fastapi import FastAPI
from dotenv import load_dotenv


log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level = getattr(logging, log_level, logging.INFO),
    format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


app = FastAPI(title="Конвертер рублей")
load_dotenv()


@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"Message": "Сервис работает"}


@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"Status": "OK"}


@app.get("/rates")
def get_rates():
    logger.info("Rates endpoint accessed: returning fixed rates")
    return {"USD": 84.9, "EUR": 94.97, "CNY": 12.67}


@app.get("/place")
def place(name: str = "Остальной Мир"):
    name = name.title()
    logger.info("Place endpoint called with name=%s", name)
    if name == "Китай":
        valute = "CNY"
    elif name == "Европа":
        valute = "EUR"
    else:
        valute = "USD"
    logger.debug("Selected currency=%s for region=%s", valute, name)
    return {"Регион": name, "Валюта": valute}


@app.get("/convert")
def convert(rub: float = 0, region: str = "Остальной Мир"):
    logger.info("Convert endpoint called: rub=%s, region=%s", rub, region)
    region = region.title()
    if rub < 0:
        logger.warning("Negative rub value received: %s. Returning 0.", rub)
        rub = 0
    if region == "Китай":
        logger.debug("Using CNY for region=%s", region)
        return {"Юани": round(rub / 12.67, 2)}
    elif region == "Европа":
        logger.debug("Using EUR for region=%s", region)
        return {"Евро": round(rub / 94.97, 2)}
    else:
        logger.debug("Using USD for region=%s", region)
        return {"Доллары": round(rub / 84.9, 2)}


@app.get("/version")
def version():
    logger.info("Version endpoint accessed")
    return {"Version": "0.1.0"}


@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "Учебный сервис")
    app_author = os.getenv("APP_AUTHOR", "Не указан")
    app_port = os.getenv("PORT", "Не указан")
    logger.info("Info endpoint accessed. App=%s, Author=%s, Port=%s", app_name, app_author, app_port)
    return {"App Name": app_name, "Author": app_author, "Port": app_port}