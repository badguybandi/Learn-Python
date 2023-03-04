import requests

API_KEY = "952f144315641aff7ab87db32840f217"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city =  input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}")

else:
    print(f"Error: {response.status_code}")

