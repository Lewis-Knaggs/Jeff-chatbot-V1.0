# Defining get weather
def getWeather():
    import requests
    import json
    api_key = "ced2064942ce7787c69e26317d70477c"
    # Type in your local latitude and longitude bellow to get your local weather fron Jff
    lat = "0"
    lon = "0"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)

    currentTemp = data["current"]["temp"]
    currentDescription = data["current"]["weather"][0]["description"]
    weather = "In your local area. The temperature is %s°C and there is %s" % (currentTemp, currentDescription)
    return weather
