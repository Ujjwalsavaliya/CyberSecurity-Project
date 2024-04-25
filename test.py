# Flask app
from flask import Flask, render_template
import requests

app = Flask(__name__)

Airport_name = 'Townsville'
Airline_name = 'Virgin Australia'

API_URL_AIRPORT = 'https://api.api-ninjas.com/v1/airports?name={Airport_name}'
API_URL_AIRLINE = 'https://api.api-ninjas.com/v1/airlines?name={Airline_name}'
API_KEY = 'NaKZK/rxLDzWVNbXHk3ABg==oPjpM3crayXZDxdF'  # Replace 'YOUR_API_KEY' with your actual API key
    
def get_airport_info(name):
    api_url = f'https://api.api-ninjas.com/v1/airports?name={Airport_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    return response.json() if response.status_code == requests.codes.ok else None

def get_airline_info(name):
    api_url = f'https://api.api-ninjas.com/v1/airlines?name={Airline_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY}) 
    return response.json() if response.status_code == requests.codes.ok else None

@app.route('/')
def index():     
    # Get airport information
    airport_info = get_airport_info(Airport_name)
    # Get airline information
    airline_info = get_airline_info(Airline_name)
    return render_template('index.html', airport_info=airport_info, airline_info=airline_info)

if __name__ == "__main__":
    app.run()

