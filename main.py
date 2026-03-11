import requests
from data_manager import DataManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
flight_data = data_manager.get_existing_flight_data()
print(data_manager.update_flight_cost(id=3, lowest_price=2))