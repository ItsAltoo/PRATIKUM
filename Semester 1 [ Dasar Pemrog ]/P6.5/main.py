# Ketikan Code Disini lalu Jalankan (Run)
mhs = ("malik","yadi","arpan","nabil","apid","malik","malik")

print(f"Isi mahasiswa :{mhs}") #Isi dari variable mhs atau isi dari Tuple
print(f"Jumlah Mahasiswa : {len(mhs)}")
print(f"Indeks 'Malik' : {mhs.index("malik")}")
print(f"Jumlah 'Malik : {mhs.count("malik")}")


# Ketikan Code Disini lalu Jalankan (Run)
data_mhs = ("Malik","2411102441250")

nama,nim = data_mhs
print(f"Nama :{nama}")
print(f"Nim :{nim}")


# Ketikan Code Disini lalu Jalankan (Run)
list_buah = ["pepaya","semangka","nanas","apel","coklat","jeruk"]
tuple_buah = tuple(list_buah)

print(tuple_buah) #Hasil dari perubahan dari list ke tuple
print(tuple_buah[2:5+1]) #menampilkan dari index ke 2 sampai ke 5


# Ketikan Code Disini lalu Jalankan (Run)
kota = ("samarinda","bandung","medan")

kota[0] = "jakarta"
print(kota) #karena tuple adalah data seperti list tetapi tidak bisa di ubah-ubah


# kota = kota + ("jakarta",)
# print(kota)



