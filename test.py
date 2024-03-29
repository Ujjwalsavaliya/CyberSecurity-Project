import requests

def get_airport_info():
    url = "https://airport-info.p.rapidapi.com/airport"
    headers = {
        "X-RapidAPI-Key": "f8901fd9e2mshea5eb425e4dc2e8p1ec6b4jsnafa09dc7acb9",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    airport_info = get_airport_info()
    for airport in airport_info:
        print(airport)
