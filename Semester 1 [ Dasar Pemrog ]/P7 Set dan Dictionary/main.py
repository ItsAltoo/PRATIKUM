# Ketikan Code Disini lalu Jalankan (Run)
buah = {"mangga",'apel','jeruk','leci'}

buah.add("kiwi")
print(buah)

buah.remove("leci")
print(buah)

# Ketikan Code Disini lalu Jalankan (Run)
set1 = {1,2,3}
set2 = {3,4,5}

union = set1.union(set2)
print(union)

interS = set1.intersection(set2)
print(interS)

diffe = set1.difference(set2)
print(diffe)


# Ketikan Code Disini lalu Jalankan (Run)
mahasiswa = {
    "nama" : "Malik Sabarullah Akbar",
    "nim" : 2411102441250,
    "jurusan" : "Informatika"
}

print(mahasiswa.get("nama"))

mahasiswa.update({"alamat" : "panjaitan"})
print(mahasiswa)

mahasiswa.pop("nim")
print(mahasiswa)


# Ketikan Code Disini lalu Jalankan (Run)
mahasiswa = {
    "dia" : "411923",
    "ya" : "421123",
    "yia" : "32192"
}

print(mahasiswa.keys())
print(mahasiswa.values())
print(mahasiswa.items())


kontak = {}

while True:
    print("\nAplikasi Pengelola Kontak Mahasiswa")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Tampilkan Semua Kontak")
    print("4. Keluar")

    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == "1":
        nim = input("Masukkan NIM Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        if nim in kontak:
            print("NIM sudah ada di dalam kontak.")
        else:
            kontak[nim] = nama
            print("Kontak berhasil ditambahkan!")

    elif pilihan == "2":
        nimHps = input("Masukkan NIM Mahasiswa yang ingin dihapus: ")
        if nimHps in kontak:
            del kontak[nimHps]
            print("Kontak berhasil dihapus!")
        else:
            print("NIM tidak ditemukan.")

    elif pilihan == "3":
        if kontak:
            print("\nDaftar Kontak Mahasiswa:")
            for nim, nama in kontak.items():
                print(f"NIM: {nim}, Nama: {nama}")
        else:
            print("Tidak ada kontak yang tersimpan.")

    elif pilihan == "4":
        print("Keluar dari aplikasi...")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
