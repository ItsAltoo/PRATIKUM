# Ketikan Code Disini lalu Jalankan (Run)
def volume_kubus(s): #pada fungsi dengan nama volume_kubus(s) dengan param s
    return s ** 3   #return mengembalikan nilai s pangkat 3
    
volume_kubus(5) #fungsi volume_kubus(5) yang di isi dengan argument 5
#dan akan menghasilkan output 125 karena 5 pangkat 3 sama saja dengan 5 x 5 x 5 = 125


# Ketikan Code Disini lalu Jalankan (Run)
def cek_genap(genap):
    if genap % 2 == 0:
        return True
    else:
        return False
    
cek_genap(3)


# Ketikan Code Disini lalu Jalankan (Run)
check_genap = lambda genap: genap % 2 == 0 #jika nilainya di modulo 2 sama dengan 0,maka nilainya true,jika tidak 0 maka false

check_genap(3) #jika argument yang di isi adalah bilang bulat maka nilainya true jika ganjil false dengan type data Boolean


# Ketikan Code Disini lalu Jalankan (Run)
def faktorial(n):
    if n == 1: #jika argument yang di masukkan sama dengan 1 maka return,jika tidak akan masuk ke opsi  else
        return 1
    else:
        return n * faktorial(n-1)#jika nilai kondisi false maka,mengembalikan nilai n adalah 5 dikalikan faktorial(5-1) => 5 * 4

faktorial(5) #memanggil fungsi faktorial dengan argument 5

#contoh alur perhitungannya:
# faktorial(5 * 4)
# faktorial(5 * 4 * 3)#
# faktorial(5 * 4 * 3 * 2)#
# faktorial(5 * 4 * 3 * 2 * 1)#
# faktorial(5 * 4 * 3 * 2)#
# faktorial(5 * 4 * 6)#
# faktorial(5 * 24)#
# faktorial(120)
# maka output yang di hasilkan 120#

# Ketikan Code Disini lalu Jalankan (Run)
index = lambda x,y: x ** y #pada fungsi lambda dengan param x dan y,dengan tugas x ** y atau  x pangkat y

index(4,3) #jika argument x = 4 dan y = 3 maka 4 x 4 x 4 = 64 atau 4 pangkat 3


# Ketikan Code Disini lalu Jalankan (Run)
angka = [1,2,3,4,5,6,7,8,9,10]

genap = list(filter(lambda x:x % 2 == 0,angka))# pada varibale genap dengan isi list dengan method filter dengan isi fungsi x % 2 == 0,pada variable atau list angka

print(genap)#dan menghasilkan bilangan genap yang ada pada list angka


# Ketikan Code Disini lalu Jalankan (Run)
def hitung(n):
    print(n) #print n atau angka yang di masukkan pada argument fungsi hitung
    if n < 10: #jika nilai 1 maka true
        hitung(n + 1) #nilai satu akan di tambkan 1,dan mengulang fungsinya dengan argument hitung(2),seterusnya hingga kondisi terpenuhi
        
        
hitung(1) # ada fungsi hitung(n) dengan argument n-nya adalah 1 atau dimulai dari angka 1