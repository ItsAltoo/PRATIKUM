from models.car import Car
from models.car_dealer import CarDealer
from models.customer import Customer

if __name__ == "__main__":
    mobil1 = Car("Civic","Honda")
    mobil2 = Car("Mustang","Ford")
    mobil3 = Car("Impreza","Subaru")
    
    customer1 = Customer("Alice")
    
    car_list = [mobil1, mobil2, mobil3]
    
    for mobil in car_list:
        dealer = CarDealer()
        dealer.add_car(mobil)
        

        print("\nKoleksi Mobil di Dealer:")
        dealer.show_collection()

        print()
        customer1.borrow_car(mobil)

        print("\nStatus Koleksi Mobil di Dealer Setelah Dipinjam:")
        dealer.show_collection()
        
        print()
        customer1.return_car(mobil)
        print("\nStatus Koleksi Mobil di Dealer Setelah Dikembalikan:")
        dealer.show_collection()
        
        print(20*"-")