from fastapi import FastAPI
from typing import Optional
#from enum import Enum

app = FastAPI()

weather_db = [{"Low" : 66, "High": 78, "Precipitation": 15, "Cloud Cover" : 50}, 
              {"Low" : 69, "High" : 80, "Precipitation" : 9, "Cloud Cover": 22}, 
              {"Low": 72, "High": 85, "Precipitation": 6, "Cloud Cover" : 10}, 
              {"Low": 68, "High" : 73, "Precipitation" :50, "Cloud Cover" :90}, 
              {"Low" : 63, "High": 70, "Precipitation": 90, "Cloud Cover" : 100}, 
              {"Low" : 65, "High": 84, "Precipitation": 7, "Cloud Cover" : 40}, 
              {"Low" : 79, "High": 87, "Precipitation": 2, "Cloud Cover" : 5}
            ]

dow_key = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

@app.get("/weather/{day_of_week}")
async def root(
    day_of_week: int = 0, rain: bool = True, num: int = 0
):
    weather = weather_db[day_of_week: day_of_week + num]

    days = []
    if not rain:
        for x in range(day_of_week, day_of_week + num):
            days.append((dow_key[x], {"Low" :weather['Low'], "High": weather['High']}))

    else:
        for i, x in enumerate(range(day_of_week, day_of_week + num)) :
            days.append((dow_key[x], weather[i]))

    return days
