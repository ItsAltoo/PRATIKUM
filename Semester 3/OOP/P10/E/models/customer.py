class Customer:
    def __init__(self, name):
        self.__name = name
        self.car_list = []

    def borrow_car(self,car):
        if not car.borrowed:
            car.borrowed = True
            self.car_list.append(car)
            print(f"{self.__name} Meminjam Mobil {car.name} dengan brand {car.brand}")
        else:
            print(f"Mobil {car.name} dengan brand {car.brand} sedang dipinjam orang lain.")    

    def return_car(self,car):
        if car in self.car_list:
            car.borrowed = False
            self.car_list.remove(car)
            print(f"{self.__name} mengembalikan Mobil {car.name} dengan brand {car.brand}")
        else:
            print(f"{self.__name} tidak meminjam Mobil {car.name} dengan brand {car.brand}")
      