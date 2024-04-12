import datetime

from fastapi import FastAPI
from zoneinfo import ZoneInfo

app = FastAPI()


@app.get("/")
async def root():
    tz = ZoneInfo("Asia/Taipei")
    now = datetime.datetime.now(tz=tz)
    return {"Datetime": f"{now:%Y:%m:%d-%H:%M:%S %Z%z}"}
