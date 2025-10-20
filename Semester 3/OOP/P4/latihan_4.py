class Kendaraan:
    def __init__(self,merk,tahun_produksi,warna):
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    def tampilkan_info(self):
        print(f"\nMerk: {self.__merk}, Tahun Produksi: {self.__tahun_produksi}, Warna: {self.__warna}")
        
    def nyalakan_mesin(self):
        print("\nMesin kendaraan dinyalakan.")
        


class Mobil(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, jumlah_pintu):
        super().__init__(merk, tahun_produksi, warna)
        self.__jumlah_pintu = jumlah_pintu

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"\nJumlah Pintu: {self.__jumlah_pintu}")
        
    def buka_pintu_bagasi(self):
        print("\nPintu bagasi mobil dibuka.")


class Motor(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, kapasitas_tangki):
        super().__init__(merk, tahun_produksi, warna)
        self.__kapasitas_tangki = kapasitas_tangki

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"\nKapasitas Tangki: {self.__kapasitas_tangki} liter")

    def nyalakan_mesin(self):
        super().nyalakan_mesin()
        print("\nBrmm... Mesin motor dinyalakan dengan kick starter!")
        
        
# Contoh penggunaan kelas
mobil1 = Mobil("Toyota", 2020, "Merah", 4)
motor1 = Motor("Yamaha", 2019, "Hitam", 15)

mobil1.tampilkan_info()
mobil1.nyalakan_mesin()
mobil1.buka_pintu_bagasi()

motor1.tampilkan_info()
motor1.nyalakan_mesin()