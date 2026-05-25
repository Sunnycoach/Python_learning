from main import weather

def test_weather():
    w = weather()
    assert w.weather_check(-5) == "Freezing"
    assert w.weather_check(5) == "Cold"
    assert w.weather_check(15) == "Cool"
    assert w.weather_check(35) == "Hot"

def test_rain():
    w = weather()
    assert w.rain_check(0.9) == "Take an umbrella"
    assert w.rain_check(0.5) == "No need for an umbrella"