class Car:
    def __init__(self,name, brand):
        self.name = name
        self.brand = brand
        self.borrowed = False
        
    def show_info(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"Mobil: {self.name}, Brand: {self.brand}, Status: {status}"
