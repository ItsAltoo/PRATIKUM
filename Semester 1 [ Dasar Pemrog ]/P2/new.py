x = ['apel','banana']
nama = input('ketik/masukkan nama anda: ')
print('banana'in x)
print('cherry'in x)
print('cherry'not in x)
print('nama anda ketika sudah di perkecil:' +nama.lower())
print('cherry'not in nama)
print('B'in nama)
print('b'in nama)
print('m'not in nama)
print('M'not in nama)

a = 5
b= 10

penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b
pembagianBulat = a // b
modulus = a % b
pangkat = a ** b

print(penjumlahan,pengurangan,perkalian,pembagian,pembagianBulat,modulus,pangkat)

x = 2411102441250
nama = "Malik Sabarullah Akbar"
print(x)
print(nama)

x = 10

x += 5
print(x)
x -= 10
print(x)
x *= 2
print(x)
x /= 2
print(x)
x %= 3
print(x)

bil1 = 5
bil2 = 3
bil3 = 5

# Sama dengan
print(bil1 == bil2)
print(bil1 == bil3)
# tidak sama dengan
print(bil1 != bil2)
# lebih besar dari
print(bil1 > bil2)
print(bil1 > bil3)
# lebih kecil dari
print(bil1 < bil2)
# lebih besar sama dengan
print(bil1 >= bil2)
# lebih kecil sama dengan
print(bil1 <= bil2)


betul = True
salah = False

#AND
print(betul and salah)
print(betul and betul)
print(True and  False)
#OR
print(betul or salah)
print(betul or betul)
print(True or  False)
#not
print(not salah)
print(not  False)

x=['buah','apel']
y=['buah','apel']
c = ['sigma','skibidiToilet','-9999 aura']
z= x

print(x is z)
print(x is y)
print(x == y)
print(x== 'apel')
print(x is c)
print(x is not c)

x = ['apel','banana']
nama = input('ketik/masukkan nama anda: ')
print('banana'in x)
print('cherry'in x)
print('cherry'not in x)
print('nama anda ketika sudah di perkecil:' +nama.lower())
print('cherry'not in nama)
print('B'in nama)
print('b'in nama)
print('m'not in nama)
print('M'not in nama)

a = 5  
b = 3 

# Operasi AND
hasil_and = a & b 
print(hasil_and)

# Operasi OR
hasil_or = a | b 
print(hasil_or)

# Operasi XOR
hasil_xor = a ^ b 
print(hasil_xor)

# Operasi NOT
hasil_not = ~a 
print(hasil_not)

# Shift kiri (menggeser 1 bit ke kiri)
hasil_shift_kiri = a << 1 
print(hasil_shift_kiri)

# Shift kanan (menggeser 1 bit ke kanan)
hasil_shift_kanan = a >> 1 
print(hasil_shift_kanan)

print('hello world') #ini juga komentar

'''
ini adalah komentar multi-baris
semua teks yang tercakup di antara tanda kutip triple
akan diabaikan oleh python
'''
print('hello,nama saya malik')
'''
ini adalah komentar multi-baris di paling bawah
semua teks yang tercakup di antara tanda kutip triple
'''

nilai1 = 2
nilai2 = 2

def proses(nilai1, nilai2):
    # Mulai - Mulai proses pengecekan
    print("Mulai proses pengecekan...")

    # Berapa nilainya? - Apakah nilainya sama?
    if nilai1 == nilai2:
        # Jika nilainya sama "true"
        kesimpulan = "Kesimpulan: nilai Anda sama."
        tindakan = "Lanjutkan aktivitas lain."
    else:
        # Jika nilainya tidak sama "false"
        kesimpulan = "Kesimpulan: nilainya beda karena nilainya memang beda."
        tindakan = "Pertimbangkan untuk nilainya sama."
    
    # Evaluasi jawaban
    print(kesimpulan)
    print(tindakan)

    print("Proses selesai.")


"""
- Mulai - Mulai proses pengecekan.
- Berapa nilainya? - Apakah nilainya sama?
- Evaluasi jawaban:
- - Jika nilainya tidak sama "false", maka:
- - - Kesimpulan: nilainya beda karna nilainya emang beda.
- - - Tindakan: Pertimbangkan untuk nilainya sama.
- - Jika nilainya sama "true", maka:
- - - Kesimpulan: nilai anda sama.
Selesai - Proses selesai, lanjutkan dengan aktivitas lain.
"""