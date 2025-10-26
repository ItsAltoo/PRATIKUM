from library.bangun_datar.lingkaran import Lingkaran
from library.bangun_datar.persegi import Persegi

if __name__ == "__main__":
    print("--- Menghitung Luas Bangun Datar (versi modular) ---")

    Lingkaran1 = Lingkaran(7)
    luas_lingkaran = Lingkaran1.hitung_luas()
    print(f"Luas Lingkaran dengan jari-jari 7 satuan adalah {luas_lingkaran:.2f}")

    Persegi1 = Persegi(5)
    luas_persegi = Persegi1.hitung_luas()
    print(f"Luas Persegi dengan sisi 5 satuan adalah {luas_persegi:.2f}")