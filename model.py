from catboost import CatBoostRegressor
import json
import os

class Model:
    model: CatBoostRegressor
    city_decode_dict: dict
    district_decode_dict: dict
    
    def __load_dicts(self, city_decode_json, district_decode_json):
        with open(city_decode_json, "r") as file:
            self.city_decode_dict = json.load(file)
        with open(district_decode_json, "r") as file:
            self.district_decode_dict = json.load(file)
    
    def __init__(self, filename: str, format = "cbm", city_decode_json = "city.json", district_decode_json = "district.json"):
        self.__load_dicts(city_decode_json, district_decode_json)
        self.model = CatBoostRegressor().load_model(filename, "cbm")
        
    def predict(self, city, floor, floors_count, rooms_count, total_meters, price, year_of_construction, living_meters, kitchen_meters, district):
        city = self.city_decode_dict[city]
        district = self.district_decode_dict[district]
        
        predictions = self.model.predict([city, floor, floors_count, rooms_count, total_meters, price, year_of_construction, living_meters, kitchen_meters, district])
        return predictions
    
if __name__ == "__main__":
    model = Model("house_predict.cbm")
    print(model.predict('odintsovo', 7, 9, 3, 81.52, 22000000, 2022, 41.0, 20.2, 'odintsovo'))