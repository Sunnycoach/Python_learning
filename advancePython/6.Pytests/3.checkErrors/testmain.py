from main import weather
import pytest

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

def test_divide():
    w = weather()
    assert w.divide(10, 2) == 5
    assert w.divide(9,3) == 3

    # with pytest.raises(ValueError, match="Cannot divide by zero"):
    #     w.divide(10, 0)

    try:
        w.divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"