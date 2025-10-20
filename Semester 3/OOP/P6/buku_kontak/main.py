from models.kontak import Kontak

if __name__ == "__main__":
    kontak1 = Kontak("Alice", "123456789")
    kontak2 = Kontak("Bob", "987654321")
    kontak3 = Kontak("Charlie", "555666777")
    
    daftar_kontak = [kontak1, kontak2, kontak3]
    
    for kontak in daftar_kontak:
        print(kontak.tampilkan_info())
        print("Nama:", kontak.get_nama())
        print("Nomor Telepon:", kontak.get_nomor_telepon())
        print()
        