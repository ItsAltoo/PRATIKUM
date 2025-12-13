# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        
        # pdb.set_trace() # <-- Untuk Debugging: Tempatkan di sini

        # --- BUG LOGIKA DISINI ---
        # Persentase tidak dibagi 100, sehingga diskon 10% dihitung sebagai 1000%
        # jumlah_diskon = harga_awal * persentase_diskon

        # code perbaikan
        jumlah_diskon = harga_awal * persentase_diskon / 100
        
        harga_setelah_diskon = harga_awal - jumlah_diskon
        harga_akhir = harga_setelah_diskon * 1.1

        return harga_akhir

# --- UJI COBA (Ini adalah test case yang akan GAGAL) ---
if __name__ == '__main__':
    calc = DiskonCalculator()
    # Input: 1000 - 10%. Hasil yang diharapkan: 900.0
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}")
    # Output: Hasil: -9000.0 (Salah)