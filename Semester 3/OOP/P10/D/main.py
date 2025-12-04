class Buku:
    def __init__(self,judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = False
        
    def tampilkan_info(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Status: {status}"
    
class Pustaka:
    def __init__(self):
        self.koleksi_buku = []
        
    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)
        
    def tampilkan_koleksi(self):
        for buku in self.koleksi_buku:
            print(buku.tampilkan_info())
            
class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        
    def pinjam_buku(self, buku):
        if not buku.dipinjam:
            buku.dipinjam = True
            self.daftar_buku.append(buku)
            print(f"{self.nama} berhasil meminjam '{buku.judul}'")
        else:
            print(f"Maaf, '{buku.judul}' sedang dipinjam orang lain.")
            
    def kembalikan_buku(self, buku):
        if buku in self.daftar_buku:
            buku.dipinjam = False
            self.daftar_buku.remove(buku)
            print(f"{self.nama} berhasil mengembalikan '{buku.judul}'")
        else:
            print(f"{self.nama} tidak meminjam '{buku.judul}'")
            
# Contoh penggunaan
buku1 = Buku("Harry Potter", "J.K. Rowling")
buku2 = Buku("The Hobbit", "J.R.R. Tolkien")

pustaka = Pustaka()
pustaka.tambah_buku(buku1)
pustaka.tambah_buku(buku2)

anggota1 = Anggota("Andi")
anggota1.pinjam_buku(buku1)
anggota1.pinjam_buku(buku2)

print("\nStatus Koleksi Pustaka:")
pustaka.tampilkan_koleksi()

anggota1.kembalikan_buku(buku1)
print("\nStatus Koleksi Pustaka Setelah Pengembalian:")
pustaka.tampilkan_koleksi()

