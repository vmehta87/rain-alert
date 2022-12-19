import requests

OWN_Endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
API_KEY = '42a6cc50cc0ca805e7af4bcc215ebc52'
API2 = '294bc3cb3dda1bd4dd8a676a6c87316a'
OWN= 'https://api.openweathermap.org/data/2.5/weather'
CITY = 'Montreal,CA'


# https://api.openweathermap.org/data/2.5/weather?q={Montreal}&appid={294bc3cb3dda1bd4dd8a676a6c87316a}

weather_params = {
    'lat': 45.501690,
    'lon': -73.567253,
    # 'id': CITY,
    'appid': API2,
}
response = requests.get(OWN, params=weather_params)
response.raise_for_status()
weather_data = response.json()
if weather_data['weather'][0]['id'] < 800:
    print('bring an umbrella!')
else:
    print('you should be fine without an umbrella!')
