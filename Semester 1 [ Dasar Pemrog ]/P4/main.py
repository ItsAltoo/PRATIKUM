# Ketikan Code Disini lalu Jalankan (Run)
umur = int(input("Berapakah umur anda? "))

if umur < 30:
    print(f"Umur anda di bawah 30,anda {umur} tahun masih muda!") 
else:
    print(f"Umur anda di atas 30,anda {umur} tahun susah tua!")
    
""" 
-pada variable umur berinput angka 25
--jika umur yang anda masukkan kurang dari 30,maka hasilnya true
---jika true aksi yang true akan di tampilkan
--jika umur yang anda masukkan lebih dari 30,maka hasilnya false
---jika false aksi yang false akan di tampilkan
"""


# Ketikan Code Disini lalu Jalankan (Run)
usia = int(input("Berapakah umur anda? "))

if usia <= 12:
    print(f"umur anda {usia},anda masih anak-anak")
elif usia <= 19:
    print(f"umur anda {usia},anda seorang remaja")
elif usia <= 59:
    print(f"umur anda {usia},anda seorang dewasa")
else:
    print(f"umur anda {usia},anda seorang lansia")
    
""" 
-variable usia yang memiliki angka 12 bertype int
--jika usia lebih kecil sama dengan 12,maka hasilnya true
---maka akan menampilkan aksi pertama
--jika usia lebih kecil sama dengan 19,maka hasilnya false
---maka hasil tidak di tampilkan
--jika usia lebih kecil sama dengan 59,maka hasilnya false
---maka hasil tidak di tampilkan
--jika usia tidak ada di salah satu kondisi,maka hasilnya false
---maka hasil tidak di tampilkan
"""


# Ketikan Code Disini lalu Jalankan (Run)
tinggi = int(input("berapa tinggi badan anda (dalam cm)?"))
berat = int(input("berapa berat badan anda (dalam cm)?"))

if tinggi < 160:
    if berat < 60:
        print("berat badan anda ideal!")
    else:
        print("berat badan anda tidak ideal!")
else:
    if berat < 70:
        print("berat badan anda ideal")
    else:
        print("berat badan anda tidak ideal")
        
""" 
-variable tinggi bernilai 155 dengan type int
-variable berat bernilai 55 dengan type int

-jika tinggi lebih kecil dari 160,maka hasilnya true
    --jika berat lebih kecil dari 60,maka hasilnya true
        ---maka akan menampilkan aksi "berat badan anda ideal!"
    --jika tidak
        ---akan menampilkan aksi "berat badan anda tidak ideal!"

-jika tidak
    --jika berat lebih kecil dari 70
        ---maka akan menampilkan aksi "berta badan anda ideal!"
    --jika tidak
        ---akan menampilkan aksi "berat badan anda tidak ideal"
        
jika variable tinggi = 155 dan variable berat = 55,maka akan menghasilkan "berat badan anda ideal!"
"""


# Ketikan Code Disini lalu Jalankan (Run)
usia = int(input("berapa usia anda? :"))
tinggi = float(input("berapa tinggi badan anda? :"))
berat = float(input("berapa berat badan anda? :"))

if 18 <= usia <= 30 and tinggi > 165 and berat < 80:
    print("anda memenuhi syarat untuk mengikuti lomba")
else:
    print("maaf,anda tidak bisa mengikuti lomba")
    


""" 
-variable usia dengan nilai 18 dengan type int
-variable tinggi dengan nilai 175 dengan type float
-variable berat dengan nilai 60 dengan type float

-jika usia lebih kecil sama dengan 18 atau lebih kecil sama dengan 30 dan tinggi lebih besar dari 165 dan berat lebih kecil dari 80
    --jika kondisinya semua terpenuhi maka akan menampilkan "anda memenuhi sayarat untuk mengikuti lomba"
-jika tidak
    --jika kondisinya tidak terpenuhi maka akan menampilkan "maaf,anda tidak bisa mengikuti lomba"
"""



# Ketikan Code Disini lalu Jalankan (Run)
input = input("apakah anda memiliki? (y/n): ").lower()
print("anda bisa mengemudi" if input == "y" else "anda tidak bisa mengemudi")

""" 
-variable input dengan opsi y/n(yes/no),jika string menggunakan huruf besar,maka akan di ubah menjadi huruf kecil dengan method .lower()

-tampilkan aksi "anda bisa mengemudi" jika input adalah y;jika tidak akan menampilkan "anda tidak bisa mengemudi"
"""


# Ketikan Code Disini lalu Jalankan (Run)
while True:
    angka = int(input("Masukkan bilangan bulat(negatif untuk berhenti): "))
    
    if angka < 0 :
        print(f"Program berhenti. {angka}")
        break
    elif angka % 2 == 0:
        print(f"angka genap {angka}")
    else:
        print(f"angka ganjil {angka}")
        
""" 
-bila benar maka:
    -variable "angka" dengan input bertype int,dengan perintah masukkan bilangan bulat(masukkan bilangan negatif untuk berhenti)
    
    -jika "angka" lebih kecil dari 0
        -maka menampilkan "program berhenti" dan program berhenti
        -break untuk memberhentikan program
    -apabila jika,angka modulus 2 sama dengan 0
        -maka tampilkan "angka genap"
    -jika tidak
        -maka tampilkan "angka ganjil"
"""


quest = input("anda ingin ngapain?,masak/mancing/main").lower()

if quest == "masak":
    print("masak indomie aja")
elif quest == "mancing":
    print("g ada teman")
elif quest == "main":
    print("main vscode aja")
else:
    print("g ush ngapa-ngapain,tidur aja")
    
""" 
-variable "quest" dengan opsi masak/mancing/main,jika string menggunakan huruf besar maka akan di ubah menjadi huruf kecil

-jika quest sama dengan "masak"
    -maka tampilkan "masak indomie aja"
-apabila jika quest sama dengan "mancing"
    -maka tampilkan "g ada teman"
-apabila jika quest sama dengan "main"
    -maka tampilkan "main vscode aja"
-jika tidak
    -maka tampilkan "g ush ngapa-ngapain,tidur aja"
"""