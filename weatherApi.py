import requests
# import mNewath
api_key = '4e1e1c04769254970177cb657701f072'
city_name = input('Enter the name of the city :  ')
def getWeather(city_name):
    # city_name = input('Enter the city name')
    apiUrl = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
    result = requests.get(apiUrl).json()
    # print(result)
    weather = result["weather"]
    # print(weather)
    main = result["main"]
    temp = round(main["temp"] - 273.00 , 2)
    feels_like = round(main["feels_like"]-273,2)
    temp_max = round(main["temp_max"]-273,2)
    temp_min = round(main["temp_min"]-273,2)
    weather_type = weather[0]['main']
    print(f"{weather_type}y weather")
    print(f"Current temperature is {temp}°C but feels like {feels_like}°C")

    print(f"Maximum temperature of the day would be  {temp_max}°C ")
    print(f"Minimum temperature of the day would be  {temp_min}°C")

getWeather(city_name)


# webbrowser.open(apiUrl)
