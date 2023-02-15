import requests
from pprint import pprint


# TODO: Put code in funcions, add if __name__==....
API_key = 'c2082fbbca8e564516d1ffcd014a34bc'
city_name = input("Please specify a city name to get a weather forecast for it: ")
base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city_name}"
weather_data = requests.get(base_url).json()
# ((dasdas.das()).dasasd()).dasasd()
pprint(weather_data)
