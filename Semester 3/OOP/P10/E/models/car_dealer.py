from .show_collection import ShowCollection

class CarDealer(ShowCollection):
    def __init__(self):
        self.car_collection = []

    def add_car(self,car):
        self.car_collection.append(car)
