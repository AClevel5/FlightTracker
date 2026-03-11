import requests
SHEET_URL = "https://api.sheety.co/14f7d1cbe8332fa058d95bac9f80e54f/flightTracker/flights"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def update_flight_cost(self, id):
        response = requests.post(f"{SHEET_URL}/{id}")
        return response.json()["Lowest Price"]

    def get_existing_flight_data(self):
        response = requests.get(SHEET_URL)
        current_flight_data = response.json()
        return current_flight_data



