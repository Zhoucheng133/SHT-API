from fastapi import FastAPI

from utils.cht import ChtSensor

app = FastAPI()
cht = ChtSensor()

@app.get("/get")
def getData():
    return cht.getSensorData()