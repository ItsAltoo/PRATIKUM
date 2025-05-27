belanjaan = []

while True:
    print("\n~~~~~~~~~~~~~pilih belanjaan anda~~~~~~~~~~~~~")
    print("1.Kangkung")
    print("2.Sabun")
    print("3.Baju")
    print("4.Biskuit")
    print("5.Tampilkan hasil belanjaan")
    print("6.Keluar")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    pilihan = input("pilih pilihan anda 1-5 :")
    
    if pilihan == "1":
        pilihan = "Kangkung"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
        
    elif pilihan == "2":
        pilihan = "Sabun"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
        
    elif pilihan == "3":
        pilihan = "Baju"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
    
    elif pilihan == "4":
        pilihan = "Biskuit"
        belanjaan.append(pilihan)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"pilihan {pilihan} anda telah di tambahkan")
        
    elif pilihan == "5":
        print("\n ~~~berikut adalah pilihan anda~~~")
        for i, pilihan in enumerate(belanjaan, 1):
                print(f"{i}. {pilihan}")
    elif pilihan == "6":
        print("Program telah di hentikan")
        break
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("pilihan hanya 1-5")
        
# Ketikan Code Disini lalu Jalankan (Run)
angka = [24,11,10,24,41,25,0]
print(f"jumlah elemen:{len(angka)}") #jumlah list yang ada pada variable angka
print(f"jumlah elemen:{min(angka)}") #menampilkan angka yang paling kecil
print(f"jumlah elemen:{max(angka)}") #menampilkan angka yang paling tinggi pada variablenya

# Ketikan Code Disini lalu Jalankan (Run)
kota = ["samarinda","bali","bontang"]

kota.append("lempake") #menambahkan value di akhir list
print(f"Hasil dari Penggunaan append :{kota}")#menampilkan hasil dari append

kota.insert(1,"bandung") #menambahkan value "bandung" ke index [1]
print(f"Hasil dari Penggunaan insert :{kota}")#menampilkan hasil dari insert

negara = ["China","Canada","Japan"]
kota.extend(negara) #menggabungkan list kota dan list negara
print(f"Hasil dari Penggunaan extend :{kota}")#menampilkan hasil dari extend


# Ketikan Code Disini lalu Jalankan (Run)
buah = ["kurma","jeruk","mangga","anggur"]


buah.pop() #menghapus value list yang akhir
print(f"Hasil dari Penggunaan pop :{buah}")#menampilkan hasil dari pop

buah.remove("jeruk") #menghapus salah satu value yang ada di list 
print(f"Hasil dari Penggunaan remove :{buah}")#menampilkan hasil dari remove

buah.clear() #menghapus semua list yang ada
print(f"Hasil dari Penggunaan clear :{buah}")#menampilkan hasil dari clear


# Ketikan Code Disini lalu Jalankan (Run)
angka = [7,6,3,4,5,2,1]

angka.sort() #menyusun variable angka dari angka terkecil hingga ke besar
print(f"Hasil dari Penggunaan sort :{angka}")#menampilkan hasil dari sort

angka.reverse() #menyusun variable angka dari angka ke besar hingga ke kecil
print(f"Hasil dari Penggunaan reverse :{angka}")#menampilkan hasil dari reverse



# Ketikan Code Disini lalu Jalankan (Run)
nilai = []

for i in range(5):
    angka = int(input(f"masukkan nilai ke-{i+1}: ")) #memasukkan nilai hingga 5 kali
    nilai.append(angka) #menambahkan value "angka" kedalam value dari "nilai" 

print(f"jumlah elemen: {len(nilai)}") #menampilkan jumlah dari nilai
print(f"jumlah terkecil: {min(nilai)}") #menampilkan nilai terkecil dari nilai
print(f"jumlah terbesar: {max(nilai)}") #menampilkan nilai terbesar dari nilai

nilaBaru = int(input(f"nilai tambahan :")) #menambahkan nilai tambahan
nilai.append(nilaBaru) #menambahkan value "nilaiBaru" kedalam value dari "nilai"
print(f"setelah nilai ditambahkan: {nilai}") #menampilkan hasil dari setelah nilai di tambahkan dengan nilaiBaru

nilai.pop() #menghapus nilai akhir 
print(f'setelah value terakhir di hapus :{nilai}') #menampilkan hasil setelah var nilai di hapus di bagian akhirnya

nilai.sort() #mengurutkan var nilai dari terkecil hingga ke besar
print(f"setelah diurutkan: {nilai}") #menampilkan hasil dari sort



