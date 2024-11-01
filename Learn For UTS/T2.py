""" 
Masukkan harga barang: 250000
Masukkan jumlah barang: 5
Total sebelum diskon: 1250000
Total setelah diskon: 11250006
"""


hargaBrg = int(input("Masukkan harga barang :"))

jmlhBrg = int(input("Masukkan Jumlah Barang yang di ingin kan :"))

total = hargaBrg * jmlhBrg

if (total >= 1000000) :
    
    print(f"Harga Awal :{total}")
    
    diskon = total * 0.1
    total = total - diskon
    
    print(f"Harga Setelah diskon :{total}")