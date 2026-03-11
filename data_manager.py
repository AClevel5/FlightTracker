import requests
SHEET_URL = "https://api.sheety.co/14f7d1cbe8332fa058d95bac9f80e54f/flightTracker/flights"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def update_flight_cost(self, id, lowest_price):
        flight_json = {
            "flight": {
                "id": id,
                "iataCode": "FRA",
                "lowestPrice": lowest_price,
        }}
        response = requests.put(f"{SHEET_URL}/{id}", json=flight_json )
        return response.json()

    def get_existing_flight_data(self):
        response = requests.get(SHEET_URL)
        current_flight_data = response.json()
        return current_flight_data



