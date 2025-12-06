### 1. Apa itu Refactoring?

Banyak orang salah mengira bahwa _coding_ itu sekali tulis langsung jadi. Padahal, _coding_ itu seperti menulis novel; butuh revisi.

**Definisi:**
Refactoring adalah proses mengubah struktur internal kode tanpa mengubah perilaku eksternalnya (hasil akhirnya tetap sama).

**Analogi Dunia Nyata: "Renovasi Dapur Restoran"**
Bayangkan sebuah restoran yang sangat sibuk. Masakannya enak (outputnya bagus), tapi dapurnya berantakan. Panci ada di lantai, pisau bercampur dengan sendok, dan koki harus berlari bolak-balik untuk mengambil garam.

- **Masalah:** Masakan tetap jadi, tapi koki cepat lelah, resiko kecelakaan tinggi, dan pelayanan jadi lambat kalau ada menu baru.
- **Solusi (Refactoring):** Anda menata ulang dapur. Anda buat rak bumbu khusus, gantung panci dengan rapi, dan bersihkan lantai.
- **Hasil:** Rasa masakan **TIDAK BERUBAH** (pelanggan tidak tahu bedanya), tapi kerja koki jadi jauh lebih cepat, efisien, dan mudah jika ingin menambah menu baru.

**Tujuan Refactoring di Python:**

- Membuat kode lebih mudah dibaca (_clean code_).
- Memudahkan _debugging_ (mencari kutu/error).
- Mempersiapkan kode untuk fitur baru.

---

### 2. Pilar Desain SOLID

Agar saat kita melakukan _refactoring_ atau membuat aplikasi baru hasilnya kokoh dan tidak mudah "roboh", kita butuh panduan. Di dunia OOP (Object-Oriented Programming), panduan itu disingkat **SOLID**.

Bayangkan SOLID sebagai 5 aturan emas dalam membangun sebuah rumah agar rumah itu awet, mudah diperbaiki, dan nyaman ditinggali.

#### **S - Single Responsibility Principle (SRP)**

- **Prinsip:** Sebuah Class (objek) hanya boleh punya **satu alasan untuk berubah**, artinya ia hanya boleh punya **satu tugas spesifik**.
- **Analogi: "Pisau Chef vs. Pisau Swiss Army"**
  Bayangkan jika Anda punya pisau yang juga ada guntingnya, ada obengnya, dan ada pembuka botolnya (Swiss Army Knife). Memang keren, tapi sangat tidak nyaman dipakai memotong bawang dalam jumlah banyak.
  - **Cara Salah:** Satu karyawan restoran bertugas memasak, mencuci piring, sekaligus menjadi kasir. Jika dia sakit, seluruh restoran tutup.
  - **Cara Benar (SRP):** Koki khusus memasak. Kasir khusus menerima uang. Jika kasir sakit, koki tetap bisa memasak.

#### **O - Open/Closed Principle (OCP)**

- **Prinsip:** Kode harus **Terbuka** untuk ditambahkan (extension), tapi **Tertutup** untuk diubah-ubah isinya (modification).
- **Analogi: "Casing HP"**
  - **Cara Benar:** Anda ingin HP Anda terlihat beda? Anda pasang _casing_ tambahan atau stiker (**Extension**). Anda tidak perlu membongkar mesin HP dan menyolder ulang _chip_-nya hanya untuk ganti warna (**Modification**).
  - Di Python, kita menggunakan _Inheritance_ (pewarisan) untuk menambah fitur tanpa mengacak-acak kode asli yang sudah berjalan baik.

#### **L - Liskov Substitution Principle (LSP)**

- **Prinsip:** Sub-kelas (anak) harus bisa menggantikan Super-kelas (induk) tanpa merusak program.
- **Analogi: "Baterai Remote TV"**
  - Remote TV Anda butuh baterai ukuran AA (Induk). Tidak peduli mereknya Alkaline, ABC, atau Panasonic (Anak), selama itu baterai AA, remote harus menyala.
  - Jika Anda memasukkan baterai AA merek tertentu lalu remote-nya meledak atau TV-nya malah mati, berarti baterai itu melanggar prinsip Liskov. Anak (baterai merek X) tidak bisa menggantikan peran Induk (konsep baterai AA).

#### **I - Interface Segregation Principle (ISP)**

- **Prinsip:** Jangan memaksa klien (pengguna class) untuk bergantung pada metode yang tidak mereka pakai.
- **Analogi: "Menu Makanan Paket Hemat"**
  - **Cara Salah:** Anda masuk restoran ingin beli Burger. Tapi restoran bilang, "Anda wajib beli Paket Besar yang isinya Burger + Pizza + Sushi + Steak." Padahal Anda cuma mau Burger. Itu membebani.
  - **Cara Benar (ISP):** Restoran memecah menu. Ada menu Burger, ada menu Pizza. Anda ambil yang Anda butuhkan saja.
  - Di Python, lebih baik buat banyak Class kecil yang spesifik daripada satu Class raksasa yang punya ratusan fungsi.

#### **D - Dependency Inversion Principle (DIP)**

- **Prinsip:** Bergantunglah pada abstraksi (konsep umum), bukan pada detail (benda konkret).
- **Analogi: "Colokan Listrik (Stopkontak)"**
  - Lampu meja Anda punya steker (colokan). Lampu itu tidak peduli listriknya datang dari PLN, dari Genset, atau dari Tenaga Surya. Lampu itu hanya peduli pada **bentuk colokan** (Interface/Abstraksi).
  - Jika Anda menyolder kabel lampu langsung ke tiang listrik PLN, itu melanggar DIP. Karena kalau PLN mati dan Anda mau ganti ke Genset, Anda harus memotong kabel dan menyolder ulang.
  - Dengan colokan standar, Anda bisa cabut-pasang sumber listrik dengan mudah.

<img src="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRG5J2P3Dc8ChEt4412GPQQI43rdv-tmcoa8L0AGUIsIV7kRP0T8ARyPhQk5KcGHVzzBUaehJ66GjkKZ0B3Gv-D2iIKVeIA4NDXMr9xQRAcYAnVppQ" />

---

### Rangkuman Singkat

1.  **Refactoring:** Bersih-bersih kode biar rapi, tanpa ubah fungsi.
2.  **S (SRP):** Satu alat, satu fungsi.
3.  **O (OCP):** Tambah fitur jangan bongkar mesin, tapi pasang aksesoris.
4.  **L (LSP):** Barang pengganti harus berfungsi sama seperti aslinya.
5.  **I (ISP):** Jangan paksa orang ambil yang tidak mereka butuhkan.
6.  **D (DIP):** Pakai colokan standar, jangan sambung kabel sembarangan.
