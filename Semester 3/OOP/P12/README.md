# Penjelasan Kode Latihan Mandiri (P12)

Kode ini merupakan implementasi sistem validasi registrasi mahasiswa yang menerapkan prinsip **SOLID**, khususnya:

1.  **Single Responsibility Principle (SRP):**

    - Kelas `RegistrationService` hanya bertanggung jawab untuk menjalankan proses registrasi.
    - Logika validasi dipisahkan ke dalam kelas-kelas aturan tersendiri (`SksLimitRule`, `PrerequisiteRule`, `JadwalBentrokRule`).

2.  **Open/Closed Principle (OCP):**

    - Sistem terbuka untuk perluasan (penambahan aturan baru) tetapi tertutup untuk modifikasi.
    - Contoh: `JadwalBentrokRule` ditambahkan sebagai aturan baru tanpa perlu mengubah kode di dalam `RegistrationService`.

3.  **Dependency Inversion Principle (DIP):**
    - `RegistrationService` tidak bergantung pada kelas konkret, melainkan bergantung pada abstraksi (interface) `IValidationRule`.
    - Hal ini memungkinkan kita untuk menyuntikkan (inject) berbagai jenis aturan validasi ke dalam service.

**Alur Program:**

1.  Data mahasiswa dibuat menggunakan dataclass `Mahasiswa`.
2.  Daftar aturan validasi dikonfigurasi dan dimasukkan ke dalam list.
3.  `RegistrationService` diinisialisasi dengan daftar aturan tersebut.
4.  Saat `register_student` dipanggil, service akan memeriksa semua aturan satu per satu. Jika ada satu saja yang gagal, registrasi ditolak.
