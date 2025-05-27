# Ketikan Code Disini lalu Jalankan (Run)
nim = 1250
angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))

penjumlahan = angka_1 + angka_2
pengurangan = angka_1 - angka_2
perkalian = angka_1 * angka_2
pembagian = angka_1 / angka_2 #kesalahan pada operasi pada pembagian
pangkat = angka_1 ** angka_2

maximum = max(angka_1, angka_2)
minimum = min(angka_1, angka_2)
pembagian_rounded = round(pembagian,2)

print(f"Hasil penjumlahan : {penjumlahan}") #kurangnya fungsi string formatting di sebelum string
print(f"Hasil pengurangan : {pengurangan}")#kurangnya fungsi string formatting di sebelum string
print(f"Hasil perkalian : {perkalian}")#kurangnya fungsi string formatting di sebelum string
print(f"Hasil pembagian : {pembagian}")#kurangnya fungsi string formatting di sebelum string
print(f"Hasil pangkat : {pangkat}")#kurangnya fungsi string formatting di sebelum string
print(f"Pembagian (dibulatkan angka 2): {pembagian_rounded}")#salahnya variable

angka1 = float(input("masukkan angka pertama :"))
angka2 = float(input("masukkan angka kedua :"))

pembulatan = round(angka2,2)
nilai_absolute = abs(angka1)
hasil_pangkat = pow(angka1,angka2)


print(f'nilai angka1 :{angka1}')
print(f"nilai angka2 : {angka2}")
print(f"hasil dari pembulatan: {pembulatan}")
print(f"hasil dari nilai absolute: {nilai_absolute}")
print(f"hasil dari pemangkatan: {hasil_pangkat}")

# Ketikan Code Disini lalu Jalankan (Run)
nama = str(input("nama saya adalah :"))

print(f"nama awal saya : {nama}")
print(nama.upper())
print(nama.lower())
print(nama.title())
print(f"panjang nama saya adalah {nama.__len__()}")

# Ketikan Code Disini lalu Jalankan (Run)
nama = input("nama saya adalah :")
nim = input("nim saya adalah :")
umur = input("umur saya adalah :")

print(f"nama saya adalah {nama},nim saya adalah {nim},dan umur saya adalah {umur}")#menggunakan f string
print("nama saya adalah {},nim saya adalah {},dan umur saya adalah {}".format(nama,nim,umur))#menggunakan .format()

# Ketikan Code Disini lalu Jalankan (Run)
angka = input("masukkan angka pertama anda :")

print(f"type data sebelum di ubah : {type(angka)}")
print(f"angka sebelum di ubah : {angka}")

angkaKedua = int(angka)

print(f"type data sesudah di ubah : {type(angkaKedua)}")
print(f"angka setelah di ubah : {angkaKedua}")

