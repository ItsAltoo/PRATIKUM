# Laporan Debugging: Analisis Bug PPN 10%

Laporan ini mendokumentasikan proses debugging menggunakan `pdb` untuk menemukan penyebab kesalahan perhitungan harga akhir, di mana PPN 10% ditambahkan secara tidak semestinya (double counting atau tidak diminta).

## Langkah-langkah Debugging

1.  **Menjalankan Program**
    Saya menjalankan script `diskon_service.py` yang telah dilengkapi dengan `pdb.set_trace()`.

    ```bash
    python diskon_service.py
    ```

2.  **Navigasi Code (`n`)**
    Setelah program berhenti di breakpoint, saya menggunakan perintah `n` (next) untuk melangkah baris demi baris melewati perhitungan diskon yang sudah diperbaiki.

    ```text
    > .../diskon_service.py(16)hitung_diskon()
    -> jumlah_diskon = harga_awal * persentase_diskon / 100
    (Pdb) n
    > .../diskon_service.py(18)hitung_diskon()
    -> harga_setelah_diskon = harga_awal - jumlah_diskon
    (Pdb) n
    > .../diskon_service.py(19)hitung_diskon()
    -> harga_akhir = harga_setelah_diskon * 1.1
    ```

## Bukti Variabel (`p`)

Pada titik ini, variabel `harga_setelah_diskon` memegang nilai yang benar (900.0). Namun, baris berikutnya (`* 1.1`) mencurigakan.

1.  **Memeriksa Harga Sebelum PPN Tambahan**
    Saya memeriksa nilai sebelum baris 19 dieksekusi sepenuhnya (atau nilai variabel inputnya).

    ```text
    (Pdb) p harga_setelah_diskon
    900.0
    ```

    _Nilai ini sudah benar sesuai ekspektasi (1000 - 10% = 900)._

2.  **Eksekusi Baris Bug**
    Saya menjalankan baris 19.

    ```text
    (Pdb) n
    > .../diskon_service.py(21)hitung_diskon()
    -> return harga_akhir
    ```

3.  **Membuktikan PPN Dihitung (Bug)**
    Saya memeriksa nilai `harga_akhir` yang dihasilkan.

    ```text
    (Pdb) p harga_akhir
    990.0
    ```

    **Analisis:**
    Perintah `p harga_akhir` menunjukkan nilai **990.0**.
    Sedangkan `p harga_setelah_diskon` adalah **900.0**.

    Selisih 90.0 ini berasal dari pengalian `* 1.1` (10%) pada baris:
    `harga_akhir = harga_setelah_diskon * 1.1`

    Ini membuktikan bahwa sistem menambahkan PPN 10% lagi setelah diskon, yang menyebabkan hasil akhir tidak sesuai dengan _test case_ yang mengharapkan **900.0**.

## Kesimpulan

Bug ditemukan pada logika penambahan PPN:

```python
harga_akhir = harga_setelah_diskon * 1.1
```

Baris ini harus dihapus atau disesuaikan karena menambahkan biaya tambahan yang tidak sesuai dengan spesifikasi tes.
