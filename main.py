import requests
from data_manager import DataManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
flight_data = data_manager.get_existing_flight_data()
