# test_diskon.py
import unittest
from diskon_service import DiskonCalculator

class TestDiskonCalculator(unittest.TestCase):

    def setUp(self):
        """Arrange: Siapkan instance Calculator."""
        self.calc = DiskonCalculator()

    def test_diskon_standar_10_persen(self):
        """Tes 1: Memastikan diskon 10% pada 1000 menghasilkan 900."""
        # Act
        hasil = self.calc.hitung_diskon(1000, 10)
        # Assert
        self.assertEqual(hasil, 900.0)

    def test_diskon_nol(self):
        """Tes 2 (Boundary): Memastikan diskon 0% tidak mengubah harga."""
        hasil = self.calc.hitung_diskon(500, 0)
        self.assertEqual(hasil, 500.0)

    def test_diskon_batas_atas(self):
        """Tes 3 (Boundary): Memastikan diskon 100% menghasilkan 0."""
        hasil = self.calc.hitung_diskon(750, 100)
        self.assertEqual(hasil, 0.0)

    def test_input_negatif(self):
        """Tes 4 (Boundary): Memastikan input diskon negatif (Jika fitur kupon tidak ada)."""
        # Asumsi: Diskon negatif dilarang dan menghasilkan harga awal
        # ACT
        hasil = self.calc.hitung_diskon(500, -5)
        # ASSERT
        self.assertGreaterEqual(hasil, 500) # Harga tidak boleh turun

if __name__ == '__main__':
    unittest.main() # Jalankan semua tes