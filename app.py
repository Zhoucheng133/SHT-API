from datetime import datetime
import os
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from utils.sht import ShtSensor

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
cht = ShtSensor()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")
# print(DIST_DIR)

@app.get("/get")
def getData():
    return cht.getSensorData()

@app.get("/get/day")
def getDay(year: int, month: int, day: int):
    try:
        target_day = datetime(year, month, day)
    except ValueError:
        return {
            "ok": False,
            "msg": "无效日期"
        }
    return cht.getDataByDay(target_day)

@app.get("/get/max")
def getMaxTemp():
    return cht.getMaxTemp()

@app.get("/get/min")
def getMinTemp():
    return cht.getMinTemp()

@app.get("/get/maxByDay")
def getMaxByDat(year: int, month: int, day: int):
    try:
        target_day = datetime(year, month, day)
    except ValueError:
        return {
            "ok": False,
            "msg": "无效日期"
        }
    return cht.getMaxByDay(target_day)

@app.get("/get/minByDay")
def getMinByDat(year: int, month: int, day: int):
    try:
        target_day = datetime(year, month, day)
    except ValueError:
        return {
            "ok": False,
            "msg": "无效日期"
        }
    return cht.getMinByDay(target_day)

@app.get("/get/recent/temperature")
def getRecentTemperature(day: Optional[str] = None):
    if day is None:
        return {"msg": "参数 day 未提供"}
    return cht.getRecentTemperature(day)

@app.get("/get/recent/humidity")
def getRecentHumidity(day: Optional[str] = None):
    if day is None:
        return {"msg": "参数 day 未提供"}
    return cht.getRecentHumidity(day)

app.mount("/", StaticFiles(directory=DIST_DIR, html=True), name="static")