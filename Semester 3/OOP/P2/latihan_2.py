class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False

    def tampilkan_info(self):
        print(
            f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}, Status Pinjam: {'Dipinjam' if self.status_pinjam else 'Tersedia'}"
        )

    def pinjam_buku(self):
        if not self.status_pinjam:
            self.status_pinjam = True
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sudah dipinjam.")

    def kembalikan_buku(self):
        if self.status_pinjam:
            self.status_pinjam = False
            print(f"Buku '{self.judul}' berhasil dikembalikan.")
        else:
            print(f"Buku '{self.judul}' tidak sedang dipinjam.")


buku_laskar_pelangi = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku_bumi_manusia = Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980)

print(buku_laskar_pelangi.tampilkan_info())
print(buku_bumi_manusia.tampilkan_info())

print("~" * 20)

print(buku_laskar_pelangi.pinjam_buku())
print(buku_bumi_manusia.pinjam_buku())
print("Status :")
print(buku_laskar_pelangi.tampilkan_info())
print(buku_bumi_manusia.tampilkan_info())

print("~" * 20)

print(buku_laskar_pelangi.kembalikan_buku())
print(buku_bumi_manusia.kembalikan_buku())
print("Status :")
print(buku_laskar_pelangi.tampilkan_info())
print(buku_bumi_manusia.tampilkan_info())
