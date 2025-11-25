import requests

def get_coordinates(location):
    res = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={location}")

    if res.ok:
        coordinates_info = res.json()
        lat = coordinates_info["results"][0]["latitude"]
        lon = coordinates_info["results"][0]["longitude"]
        return lat, lon
    else:
        return {}

def get_weather_data(lat, lon):
    res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
    if res.ok:
        weather_info = res.json()
        return weather_info
    else:
        return {}

def main():
    user_location = input("Where do you live?: ")
    lat, lon = get_coordinates(user_location)
    return get_weather_data(lat, lon)

if __name__ == "__main__":
    main()
