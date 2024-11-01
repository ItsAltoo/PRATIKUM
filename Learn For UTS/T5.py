""" 
Materi: Tipe Data Dasar, List, dan Iterasi
Buatlah program yang meminta pengguna untuk memasukkan nama dan harga beberapa barang (minimal 5 barang). Simpan nama barang dalam list dan harga dalam list terpisah. Program kemudian menghitung total harga semua barang, serta menampilkan barang yang memiliki harga tertinggi dan terendah.

Masukkan jumlah barang: 5
Masukkan nama barang 1: Sabun
Masukkan harga barang 1: 10000
Masukkan nama barang 2: Shampoo
Masukkan harga barang 2: 25000
Masukkan nama barang 3: Pasta gigi
Masukkan harga barang 3: 15000
Masukkan nama barang 4: Minyak Goreng
Masukkan harga barang 4: 20000
Masukkan nama barang 5: Beras
Masukkan harga barang 5: 50000
Total harga: 120000
Barang dengan harga tertinggi: Beras
Barang dengan harga terendah: Sabun
"""

total_harga = []
nama_barang = []

jumlah_barang = int(input(f"Masukkan jumlah barang anda :"))

for i in range(1,jumlah_barang+1):
    
    nama = input(f"Masukkan nama barang {i} :")
    harga = int(input(f"Masukkan harga barang {i} :"))
    
    total_harga.append(harga)
    nama_barang.append(nama)
    

harga_terbesar = max(total_harga)
harga_terkecil = min(total_harga)

index_terbesar = total_harga.index(harga_terbesar)
index_terkecil = total_harga.index(harga_terkecil)

print(f"Total harga :{sum(total_harga)}")
print(f"Barang dengan harga tertinggi :{nama_barang[index_terbesar]} dengan harga :{harga_terbesar}")
print(f"Barang dengan harga terendah :{nama_barang[index_terkecil]} dengan harga :{harga_terkecil}")