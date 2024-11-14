class WeatherData:
    def __init__(self,city):
        self.city = city
        self.weather_data = None #because we have no data
        
        
    def fetch_weather_data(self):
        data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}}   
        
        if self.city in data:#this is grabbing the city in the data
            self.weather_data = data[self.city]# weather_data is the information im getting from the"data"
            print(f"Data fetch for {self.city} successfully")
        else: print("Weather data could not be fecthed")
        
class ParseWeatherData:
    def __init__(self,weather_data):
        self.weather_data = weather_data
        
    def temp(self):
        if self.weather_data:#
            return self.weather_data["temperature"] # at the key of tempurature
        else: print("Not found")
        return None #So that it doesnot continue on
    def condition(self):
        if self.weather_data:#
            return self.weather_data["condition"] # at the key of tempurature
        else: print("Not found")
        return None
    def humidity(self):
        if self.weather_data:#
            return self.weather_data["humidity"] # at the key of tempurature
        else: print("Not found")
        return None
    
    def display_data(self):
        print(f"City: {self.weather_data["city"]}, Temp: {self.weather_data["temperture"]} Condition: {self.weather_data["condition"]} Humditity: {self.weather_data["humidity"]} ")    
        
        
def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        elif city.lower() == 'new york' :
                        
        elif city.lower() == 'london':
            pass
        elif city.lower() == 'tokyo': 
            pass
        

if __name__ == "__main__":
    main()  
        
        
        
