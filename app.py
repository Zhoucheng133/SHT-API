from datetime import datetime
from fastapi import FastAPI

from utils.cht import ChtSensor

app = FastAPI()
cht = ChtSensor()

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
