from main import weather_check
import pytest

@pytest.mark.parametrize("temp, expected", [
    (-5, "Freezing"),
    (5, "Cold"),
    (15, "Cool"),
    (25, "Warm"),
    (35, "Hot")
])
def test_weather_check(temp, expected):
    assert weather_check(temp) == expected