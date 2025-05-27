# Ketikan Code Disini lalu Jalankan (Run)
import tabung #import/mengambil source code yang ada di tabung.py

r = 7
t = 10

volume = tabung.volumeTabung(r,t) #jika ingin mengambil function yang ada di tabung kalian perlu " . " untuk bsa mengambil functionnya dengan param r = 7 dan t = 10
print("volume tabung :",volume) #dan memanggil variable volume yang berisi function yg ada di tabung

print(f"hasil volume tabung : {tabung.volumeTabung(7,10):,.2f}") #ini hasilnya jika ingin dibuat lebih mudah di baca

# Ketikan Code Disini lalu Jalankan (Run)
import tabung

print(f"{dir(tabung)}") #menampilkan hasil info yang ada di dalam tabung.py

# Ketikan Code Disini lalu Jalankan (Run)
import aritmatika #di dalam aritmatika memiliki fungsi tambah(),kurang(),kali(),dan bagi()

a = 10
b = 5

print(f""" 
tambah : {aritmatika.tambah(a,b)} => menampilkan fungsi tambah dengan nilai a = 10 dan b =5 dengan hasil = 15
kurang : {aritmatika.kurang(a,b)} => menampilkan fungsi kurang dengan nilai a = 10 dan b =5 dengan hasil = 5
kali : {aritmatika.kali(a,b)} => menampilkan fungsi kali dengan nilai a = 10 dan b =5 dengan hasil = 50
bagi : {aritmatika.bagi(a,b)} => menampilkan fungsi bagi dengan nilai a = 10 dan b =5 dengan hasil = 2.0 atau 2
""")


# Ketikan Code Disini lalu Jalankan (Run)
import konversi

suhu = float(input('masukkan suhu :'))
opsi = input('masukkan konversi yang anda inginkan [CtoF , FtoC , CtoK , KtoC] :')

if opsi == "CtoF":
    print(konversi.celciusToFahrenheit(suhu))
elif opsi == "FtoC":
    print(konversi.fahrenheitToCelcius(suhu))
elif opsi == "CtoK":
    print(konversi.celciusToKelvin(suhu))
elif opsi == "KtoC":
    print(konversi.kelvinToCelcius(suhu)) 
else:
    print("opsi yang anda pilih tidak ada")   

    

# Ketikan Code Disini lalu Jalankan (Run)
from aritmatika import tambah #mengambil fungsi tambah di aritmatika ini adalah user defined
from random import randint # mengambil fungsi randint di random ini adalah modularisasi built-in

print(f""" 
angka random 1-10 : {randint(1,10)} => menghasilkan angka random dari 1 hingga 10
pertambahan dari bilangan acak : {tambah(randint(1,10),randint(1,10))} => menambah angka random 1 - 10 dengan keduanya juga random
pertambahan : {tambah(2,2)} => menambah nilai a = 2 dan b = 2 dengan hasil 4
info dari modul fungsi tambah pada aritmatika : {dir(tambah)} => menampilkan nama-nama variabel, fungsi, kelas, dll pada fungsi tambah
info dari modul fungsi randint  pada random : {dir(randint)} => menampilkan nama-nama variabel, fungsi, kelas, dll pada fungsi randint
""")
