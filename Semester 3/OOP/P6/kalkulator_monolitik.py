import math

class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * (self.radius**2)


class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

if __name__ == "__main__":
    print("--- Menghitung Luas Bangun Datar (versi modular) ---")

    Lingkaran1 = Lingkaran(7)
    luas_lingkaran = Lingkaran1.hitung_luas()
    print(f"Luas Lingkaran dengan jari-jari 7 satuan adalah {luas_lingkaran:.2f}")

    Persegi1 = Persegi(5)
    luas_persegi = Persegi1.hitung_luas()
    print(f"Luas Persegi dengan sisi 5 satuan adalah {luas_persegi:.2f}")
