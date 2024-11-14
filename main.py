from weather_data import get_detailed_forecast as gdf
from weather_data import display_weather as dw

def main():
    
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = gdf(city)#
        else:
            forecast = dw(city)
        print(forecast)
    
if __name__ == "__main__":
    main()