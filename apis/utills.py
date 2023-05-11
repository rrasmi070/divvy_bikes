import requests
import json

class Divvy_bike_apis:
    def __init__(self) -> None:
        self.station_status = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
        self.free_bike_status = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
    def station_status_api(self):
        station_details_json = requests.get(self.station_status).json()
        # print(station_details_json['data']['stations'],"===================>")
        return station_details_json['data']['stations'] 
        
    def free_bike_status_api(self):
        free_bike_status_json = requests.get(self.free_bike_status).json()
        return free_bike_status_json['data']['bikes'] 
        