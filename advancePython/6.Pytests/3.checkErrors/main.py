class weather:

    def weather_check(self, temp):
        if temp < 0:
            return "Freezing"
        elif temp < 10:
            return "Cold"
        elif temp < 25:
            return "Cool"
        else:
            return "Hot"
    
    def rain_check(self, rain_chance:float):
        if rain_chance > 0.7:
            return "Take an umbrella"
        else:
            return "No need for an umbrella"
    

    def divide(self, a:float, b:float):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b