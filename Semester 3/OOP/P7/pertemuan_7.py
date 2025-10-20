import math

class KalkulatorLingkaran:
    def __init__(self, radius):
        self.__radius = 0
        self.set_radius(radius)
        print(f"Objek lingkaran dengan radius {self.__radius} telah dibuat.")

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius harus lebih besar dari nol. Mengatur radius ke 1.")
            self.__radius = 1
        
    def hitung_luas(self):
        return math.pi * (self.__radius ** 2)
    
    def hitung_keliling(self):
        return 2 * math.pi * self.__radius

lingkaran1 = KalkulatorLingkaran(7)
luas_lingkaran1 = lingkaran1.hitung_luas()
keliling_lingkaran1 = lingkaran1.hitung_keliling()

print(f"\nRadius Lingkaran 1: 7")
print(f"Luas Lingkaran 1: {luas_lingkaran1:.2f}")
print(f"Keliling Lingkaran 1: {keliling_lingkaran1:.2f}")

from datetime import datetime

class LogPesan:
    def __init__(self, pengirim, pesan):
        self.__pengirim = pengirim
        self.__pesan = pesan
        self.__timestamp = datetime.now()
        
    def tampilkan_log(self):
        waktu_terformat = self.__timestamp.strftime("%d %B %Y, Pukul %H:%M:%S")
        print("--- log pesan ---")
        print(f"Waktu: {waktu_terformat}")
        print(f"Pengirim: {self.__pengirim}")
        print(f"Pesan: {self.__pesan}")
        
pesan1 = LogPesan("Alice", "Halo, bagaimana kabarmu?")
pesan1.tampilkan_log()

pesan2 = LogPesan("Bob", "Aku baik, terima kasih!")
pesan2.tampilkan_log()
