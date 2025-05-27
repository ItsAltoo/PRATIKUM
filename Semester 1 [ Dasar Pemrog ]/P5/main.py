# Ketikan Code Disini lalu Jalankan (Run)
for i in range (-2,15):
    print(i,end=" ")
print("looping pertama selesai")

for i in range(0,21,2):
    print(i, end=" ")
print("looping kedua selesai")

for char in "Malik":
    print(char,end=" ")
print("looping ketiga selesai")


# Ketikan Code Disini lalu Jalankan (Run)
i = 1
while i <= 50:
    print(i,end=" ")
    i += 1
print("Looping pertama telah selesai")

i= 1
while i < 500:
    if i % 2 != 0:
        print(i,end=" ")
    i += 1
print("Looping kedua telah selesai")    

i = 0
while True:
    if i == 50:
        print("Print dihentikan")
        break
    print(i,end=" ")
    i += 1
print("Looping ketiga telah selesai")



# Ketikan Code Disini lalu Jalankan (Run)

for i in range(1,100):
    if i % 3 == 0 and i % 7 == 0:
        print("Looping telah di hentikan")
        break
    print(i, end=' ')
    
""" 
untuk i di range/jarak 1 hingga 100,
    jika i modulus 3 sama dengan 0 dan i modulus 7 sama dengan 0,
        maka menampilkan 1 hingga 20,dan looping di hentikan dengan method break
"""

for i in range(1,21):
    if i % 2 != 0:
        continue
    print(i,end=' ')
    
""" 
untuk i di range/jarak 1 hingga 21
    jika i modulus 2 dan tidak sama dengan 0,maka method continue akan melewati bilangan ganjil
dan hanya menampilkan bilangan genap
"""


# Ketikan Code Disini lalu Jalankan (Run)
for i in range(1,6):
    for j in range (1,6):
        print(i * j,end=' ')
    print()
    
""" 
untuk i di range 1 hingga 6,dan
    untuk j di range 1 hingga 6
        dan print i * j
        dengan cara kerja seperti P = i x [Jn]
    jadi,baris pertama akan menampilkan 1,2,3,4,5 
    dan baris kedua akan menampilkan 2,4,6,8,10
dan seterusnya hingga baris ke 5
"""


# Ketikan Code Disini lalu Jalankan (Run)
n = int(input("Masukkan bilangan bulat: "))

for i in range (1, n+1):
    if i % 2 == 0:
        print(i)
        
""" 
variable n dengan input-an pada user,dengan type int

untuk i di range/jarak dari 1 hingga n adalah 10 dan di tambahkan 1
    jika i modulus/sisa bagi 2 sama dengan 0
        dan tampilkan hasil i hingga n/menampilkan bilangan genap dari 2 hingga 10
"""


# Ketikan Code Disini lalu Jalankan (Run)
while True:
    angka = int(input("Masukkan bilangan bulat: "))
    if angka % 5 == 0:
        print("Anda memasukkan kelipatan 5, program di hentikan, ")
        break
    else:
        print("Bukan kelipatan 5,coba lagi.")
        
""" 
apabila true,maka 
    variable angka dengan input-an dari user,dengan type int
        jika angka modulus/sisa bagi dari 5
            maka looping akan di hentikan.
        jika bukan modulus 5,maka
            looping akan di ulangi hingga,user memasukkan angka modulus 5
"""


