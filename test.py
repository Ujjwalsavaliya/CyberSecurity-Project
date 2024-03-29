from flask import Flask

app = Flask(__name__)
import requests

# Function to make API request and return the data
def get_airports():
    url = "https://airport-info.p.rapidapi.com/airport"
    headers = {
        "X-RapidAPI-Key": "f8901fd9e2mshea5eb425e4dc2e8p1ec6b4jsnafa09dc7acb9",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    airport_data = response.json()
    return airport_data

# Route to display airport data
@app.route('/airports')
def airports():
    airport_data = get_airports()
    return airport_data

if __name__ == '__main__':
    app.run()
