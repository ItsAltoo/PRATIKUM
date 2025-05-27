# Ketikan Code Disini lalu Jalankan (Run)
with open('data_diri.txt','w')as file: #membuka atau membuat jika file tidak di temukan,dengan mode w atau write
    file.write('Nama lengkap : Malik \n') #Menulis isi dari Nama Lengkap ke dalam data_diri.txt
    file.write('NIM : 2411102441250 \n') #Menulis isi Nim ke dalam data_diri.txt
    
with open('data_diri.txt','r') as file: # Membuka File data_diri.txt dengan mode r atau read
    isi = file.read() # membuat variable dengan isi membaca file data_diri.txt
    print(isi) # menampilkan variable atau isi filenya
    
    
    
# Ketikan Code Disini lalu Jalankan (Run)
daftar_nama = ['malik\n','budi\n','asep\n'] 
with open('daftar_nama.txt','w')as file : #Membuka atau membuat file daftar_nama.txt dengan mode w atau write
    file.writelines(daftar_nama) #Menulis dengan bentuk list pada variable daftar_nama
    
with open('daftar_nama.txt','r')as file: #Membuka atau membuat file daftar_nama.txt dengan mode r atau read
    for nama in file: #Melakukan perulangan pada isi file daftar_nama.txt
        print(nama.strip()) #Menampilkan isi pada file
        

# Ketikan Code Disini lalu Jalankan (Run)
with open('daftar_nama.txt','a')as file: #Membuka atau membuat file daftar_nama.txt dengan mode a atau append
    file.write("Juan\n")#Menulis dan menambah tanpa harus menimpa isi sebelumnya kedalam file

with open('daftar_nama.txt','r')as file: #Membuka atau membuat file dengan mode r atau read
    print(file.read()) # Menampilkan isi file 
    
    
# Ketikan Code Disini lalu Jalankan (Run)
import os #meng-import os agar bisa menghapus file

while True:
    inpt = input("""Pilih Opsi : 
                 1.Menghapus file daftar nama
                 2.Menghapus data diri
                 3.Exit
                 """)

    if inpt == '1': #jika inputan memilih opsi 1 program ini di jalankan
        choose = input('Ingin menghapus file daftar nama (y/n)? :')
        if choose == 'y' or choose == 'Y': #Jika input adalah y atau Y
            os.remove('daftar_nama.txt') #os.remove untuk menghapus file
        elif choose == 'n' or choose == 'N': #jika input adalah n/N
            break #membatalkan penghapusan
    elif inpt == '2': #jika inputan memilih opsi 2 program ini di jalankan
        choose = input('Ingin menghapus file data diri (y/n)? :')
        if choose == 'y' or choose == 'Y':#Jika input adalah y atau Y
            os.remove('data_diri.txt') #os.remove untuk menghapus file
        elif choose == 'n' or choose == 'N':#jika input adalah n/N
            break #membatalkan penghapusan
    elif inpt == '3':
        break #keluar dari opsi penghapusan
    else:
        print('Opsi tidak ditemukan')
        
        

import os

class DataMahasiswa:
    def __init__(self,fullName,nim):
        self.fullName = fullName
        self.nim = nim
    
    def tambah_mahasiswa(self):
        DB_NAME = 'db/data_mahasiswa.txt'
        with open(DB_NAME,'a') as file:
            dataMhs = f""" 
Nama lengkap :{self.fullName} 
NIM :{self.nim} 
            """
            file.write(dataMhs)
            print(30*'~','\n')
            print(f'Data anda telah di tambahkan ke dalam "{DB_NAME}"\n')
            print(30*'~','\n')

class Kehadiran:
    def __init__(self,name,absen):
        self.name = name
        self.absen = absen
    
    def tambahKehadiran(self):
        with open('db/kehadiran.txt','a')as file:
            absen_data = f""" 
{self.name},Telah {self.absen}            
            """
            file.write(absen_data)
            
    def cekKehadiran():
        with open('db/kehadiran.txt','r')as file:
            print(file.read())

class BacaData:
    def bacaData():
        with open('db/data_mahasiswa.txt','r')as file:
            print(file.read())

class HapusData:
    def hapusData():
        DATA = ['db/data_mahasiswa.txt','db/kehadiran.txt']
        
        while True:
            print(f""" 
1.Hapus Data ke-1 = {DATA[0]}
2.Hapus Data ke-2 = {DATA[1]}
3.Exit
              """)
            inpt = input("Pilih Opsi :")

            if inpt == '1': #jika inputan memilih opsi 1 program ini di jalankan
                choose = input(f'Ingin menghapus file {DATA[0]} (y/n)? :')
                if choose == 'y' or choose == 'Y': 
                    os.remove(DATA[0]) #os.remove untuk menghapus file
                elif choose == 'n' or choose == 'N':
                    break
            elif inpt == '2':
                choose = input(f'Ingin menghapus file {DATA[1]} (y/n)? :')
                if choose == 'y' or choose == 'Y':
                    os.remove(DATA[1]) #os.remove untuk menghapus file
                elif choose == 'n' or choose == 'N':
                    break


#Main
while True:
    print(7*'~'," Welcome ",7*'~')
    print('1.Tambah Data Mahasiswa      5.Hapus Data')
    print('2.Absen Kehadiran            6.Exit Program')
    print('3.Cek Kehadiran Mahasiswa    ')
    print('4.Cek Data Mahasiswa\n         ')
    
    
    opsi = int(input("Pilih Opsi :"))
    
    if opsi == 1:
        fullName = input('Masukkan Nama Lengkap Anda :')
        nim = input('Masukkan Nim Anda :')
        tambah_mhs = DataMahasiswa(fullName,nim)
        tambah_mhs.tambah_mahasiswa()
    elif opsi == 2:
        name = input('Masukkan Nama :')
        absen = input('Hadir/Tidak Hadir :')
        kehadiran = Kehadiran(name,absen)
        kehadiran.tambahKehadiran()
    elif opsi == 3:
        Kehadiran.cekKehadiran()
    elif opsi == 4:
        BacaData.bacaData()
    elif opsi == 5:
        HapusData.hapusData()
    elif opsi == 6:
        break
    else:
        print('Opsi Tidak Ada')

