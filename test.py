from flask import Flask, render_template
import requests

app = Flask(__name__)
name = 'Townsville'
API_URL_AIRPORT = 'https://api.api-ninjas.com/v1/airports?name={name}'
API_URL_AIRLINE = 'https://api.api-ninjas.com/v1/airlines?name=Virgin'
API_KEY = 'NaKZK/rxLDzWVNbXHk3ABg==oPjpM3crayXZDxdF'  # Replace 'YOUR_API_KEY' with your actual API key
    
def get_airport_info(name):
    api_url = f'https://api.api-ninjas.com/v1/airports?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    return response.json() if response.status_code == requests.codes.ok else None

def get_airline_info(name):
    api_url = f'https://api.api-ninjas.com/v1/airlines?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY}) 
    return response.json() if response.status_code == requests.codes.ok else None

@app.route('/')
def index():     

    # Get airport information
    airport_info = get_airport_info(name)
    if airport_info:
        # Get airline information
        airline_info = get_airline_info('Virgin Australia')
        if airline_info:
            return render_template('index.html', airport_info=airport_info, airline_info=airline_info)
        else:
            return 'Error fetching airline information'
    else:
        return 'Error fetching airport information'

if __name__ == "__main__":
    app.run()
