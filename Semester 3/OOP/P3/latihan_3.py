class Karyawan:
    def __init__(self, id, nama, gaji):
        self.__id_karyawan = id
        self.__nama_karyawan = nama
        self.__gaji_karyawan = gaji

    # Getter
    def get_id(self):
        return f"Id Karyawan: {self.__id_karyawan}"

    def get_nama(self):
        return f"Nama Karyawan: {self.__nama_karyawan}"

    def get_gaji(self):
        return f"Gaji Karyawan: {self.__gaji_karyawan}"

    # Setter
    def set_nama(self, nama):
        if nama == "":
            print("Nama tidak boleh kosong")
        else:
            self.__nama_karyawan = nama
            print("Nama karyawan berhasil diubah")

    def set_gaji(self, gaji):
        if gaji <= 0:
            print("Gaji tidak boleh negatif")
        else:
            self.__gaji_karyawan = gaji
            print("Gaji karyawan berhasil diubah")

karyawan_1 = Karyawan(1, "Andi", 5000000)

print(karyawan_1.get_id())    # Output: 1
print(karyawan_1.get_nama())  # Output: Andi
print(karyawan_1.get_gaji())  # Output: 5000000

print("\nSetelah diubah")

karyawan_1.set_nama("")
karyawan_1.set_gaji(-3000000)

print("\nSetelah diubah")
karyawan_1.set_gaji(6000000)
print(karyawan_1.get_nama())  # Output: Andi
print(karyawan_1.get_gaji())  # Output: 6000000
print(karyawan_1.get_id())    # Output: 1