# Ketikan Code Disini lalu Jalankan (Run)
class Mahasiswa:
    #di bawah ini adalah variable yang bernilai kosong,yang akan di isi kedepannya
    nama = ""
    nim = "" 
    jurusan = ""
    
    def __init__(self,n,u,j): 
        self.nama = n #menambahkan nilai n ke dalam nama
        self.nim = u  #menambahkan nilai u ke dalam nim
        self.jurusan = j #menambahkan nilai j ke dalam jurusan
        
    def info(self):
        print(f"Nama saya {self.nama},Nim : {self.nim},Prodi {self.jurusan}")
        
mhs = Mahasiswa("Malik",2411102441250,"TI") #mengisi nilai n , u , j
mhs.info() #menampilkan fungsi info() pada class

# __init__adalah method khusus yang dijalankan otomatis ketika objek baru dibuat.

# Ketikan Code Disini lalu Jalankan (Run)
class Mahasiswa:
        nama = ""
        nim = "" 
        jurusan = ""
        
        def __init__(self,n,u,j): 
                self.nama = n 
                self.nim = u
                self.jurusan = j
                
        def info(self):
                print(f"Nama saya {self.nama},Nim : {self.nim},Prodi {self.jurusan}")
                
        def perkenalan(self):
                print(f"Halo, nama saya {self.nama}. Saya mahasiswa dengan NIM {self.nim} dari jurusan {self.jurusan}.")

mhs1 = Mahasiswa('malik',2411102441250,"TI")

mhs1.perkenalan()


# Ketikan Code Disini lalu Jalankan (Run)
class PersegiPanjang:
    # pada variable dibawah ini dengan type data integer yang akan di kunakan kedepannya
    panjang = int() 
    lebar = int()
    
    def __init__(self,p,l):
        self.panjang = p
        self.lebar = l
        
    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2* (self.panjang + self.lebar)
    
pp = PersegiPanjang(4,5) #nilai p = 4 dan l = 5
print('Luas',pp.luas()) # memanggil fungsi luas() yang ada di kelas PersegiPanjang
print('Keliling',pp.keliling()) # memanggil fungsi keliling() yang ada di kelas PersegiPanjang


# Ketikan Code Disini lalu Jalankan (Run)
class Lingkaran:
    pi = 3.14
    # jari_jari = int() 
    
    def __init__(self,j):
        self.jari_jari = j
        
    def luas(self):
        return self.pi * (self.jari_jari ** 2)
    
    def keliling(self):
        return 2* self.pi * self.jari_jari
    
circle = Lingkaran(5)
print('luas lingkaran :',circle.luas())
print('keliling lingkaran :',circle.keliling())


# Ketikan Code Disini lalu Jalankan (Run)
class Karyawan:
    def __init__(self,nama,gaji,jabatan):
        self.nama = nama
        self.gaji = gaji
        self.jabatan = jabatan
        
    def kenaikanGaji(self):
        if self.jabatan == "Manager":
            self.gaji *= 1.10
        elif self.jabatan == "Staf":
            self.gaji *= 1.05
        
    def info(self):
        print(f""" 
              Nama : {self.nama}
              Gaji : {self.gaji:,.2f}
              Jabatan : {self.jabatan}
              """)
        
karyawan1 = Karyawan("ahmad",2000000,"Staf")
karyawan2 = Karyawan("Bayu",7000000,"Manager")

karyawan1.kenaikanGaji()
karyawan1.info()

karyawan2.kenaikanGaji()
karyawan2.info()


# Ketikan Code Disini lalu Jalankan (Run)
class Karyawan:
    def __init__(self,nama,gaji,jabatan):
        self.nama = nama
        self.gaji = gaji
        self.jabatan = jabatan
        
    def kenaikanGaji(self):
        if self.jabatan == "Manager":
            self.gaji *= 1.10
        elif self.jabatan == "Staf":
            self.gaji *= 1.05
        
    def info(self):
        print(f""" 
Nama : {self.nama}
Gaji : {self.gaji:,.2f}
Jabatan : {self.jabatan}
              """)


class KaryawanIT(Karyawan):
    def __init__(self, nama, gaji, jabatan, keahlian):
        # Memanggil konstruktor kelas induk (Karyawan)
        super().__init__(nama, gaji, jabatan)
        self.keahlian = keahlian

    # Menambahkan method info untuk mencetak informasi lengkap
    def info(self):
        super().info()  # Memanggil info dari kelas induk
        print(f"Keahlian: {self.keahlian}")

# Contoh penggunaan
karyawan_it = KaryawanIT("Jessnolimit", 12345, "Hyper", "fanny")
karyawan_it.info()



class Mobil:
    def jalan(self):
        print("Mobil berjalan di jalan raya 300km.")

# Kelas Motor
class Motor:
    def jalan(self):
        print("Motor melaju dengan kecepatan tinggi 250 km.")

# Fungsi untuk memanggil method jalan pada objek kendaraan
def test_jalan(kendaraan):
    kendaraan.jalan()

# Membuat objek dari kedua kelas
mobil = Mobil()
motor = Motor()

# Memanggil method jalan menggunakan polimorfisme
test_jalan(mobil)  # Output: Mobil berjalan di jalan raya.
test_jalan(motor)  # Output: Motor melaju dengan kecepatan tinggi.