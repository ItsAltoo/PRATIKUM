class Kontak:
    def __init__(self, nama, nomor_telepon):
        self.__nama = nama
        self.__nomor_telepon = nomor_telepon

    def tampilkan_info(self):
        return f"Nama: {self.__nama}, Nomor Telepon: {self.__nomor_telepon}"

    # getter
    def get_nama(self):
        return self.__nama

    def get_nomor_telepon(self):
        return self.__nomor_telepon

    # setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_nomor_telepon(self, nomor_telepon):
        self.__nomor_telepon = nomor_telepon
