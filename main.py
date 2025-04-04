from fastapi import FastAPI
from astral import moon
from datetime import date

app = FastAPI()

@app.get("/moon-phase")
def get_moon_phase():
    today = date.today()
    phase = moon.phase(today)
    
    if phase < 1:
        phase_name = "New Moon"
    elif 1 <= phase < 7:
        phase_name = "Waxing Crescent"
    elif 7 <= phase < 14:
        phase_name = "First Quarter"
    elif 14 <= phase < 21:
        phase_name = "Full Moon"
    elif 21 <= phase < 28:
        phase_name = "Last Quarter"
    else:
        phase_name = "New Moon"

    return {"date": today.isoformat(), "moon_phase": phase_name}

from astral import LocationInfo
from astral.sun import sun

@app.get("/sunrise-sunset")
def get_sunrise_sunset(city: str = "New Delhi", region: str = "India", latitude: float = 28.6139, longitude: float = 77.2090):
    loc = LocationInfo(city, region, "Asia/Kolkata", latitude, longitude)
    s = sun(loc.observer)
    
    return {
        "city": city,
        "sunrise": s["sunrise"].isoformat(),
        "sunset": s["sunset"].isoformat()
    }
