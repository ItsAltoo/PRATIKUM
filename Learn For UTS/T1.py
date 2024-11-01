""" 
Soal/Project 1: Pengolahan Nilai Mahasiswa (Iterasi dan List)

Masukkan jumlah mahasiswa: 5
Masukkan nilai UTS mahasiswa 1: 75
Masukkan nilai UTS mahasiswa 2: 80
Masukkan nilai UTS mahasiswa 3: 90
Masukkan nilai UTS mahasiswa 4: 60
Masukkan nilai UTS mahasiswa 5: 85
Rata-rata nilai UTS: 78.0
Nilai tertinggi: 90
Nilai terendah: 60
"""

from statistics import mean

nilaiUTS = []

for i in range(1,5+1):
    nilai = int(input(f"masukkan nilai mahasiswa ke-{i} :"))
    nilaiUTS.append(nilai)
    
    for j,nilai in enumerate(nilaiUTS,1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Ini adalah nilai mahasiswa ke-{i} = {nilai}")
        print(f"Ini Adalah Isi Dari Nilai UTS : {nilaiUTS}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


print(f"Ini adalah Nilai Rata-Rata : {mean(nilaiUTS)}")
print(f"Ini adalah Nilai Tertinggi : {max(nilaiUTS)}")
print(f"Ini adalah Nilai Terendah : {min(nilaiUTS)}")
    
