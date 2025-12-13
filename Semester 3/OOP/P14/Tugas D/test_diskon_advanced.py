# test_diskon_advanced.py
import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):
    
    def setUp(self):
        self.calc = DiskonCalculator()

    def test_float_calculation(self):
        """
        Tes 5: Uji nilai float yang kompleks.
        Input: 999, Diskon 33%.
        Perhitungan Manual:
          Diskon = 999 * 0.33 = 329.67
          Bayar  = 999 - 329.67 = 669.33
        """
        # Act
        hasil = self.calc.hitung_diskon(999, 33)
        
        # Assert
        # Menggunakan assertAlmostEqual karena operasi float sering memiliki
        # selisih desimal sangat kecil (misal: 669.33000000001)
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_edge_case_zero_price(self):
        """
        Tes 6: Uji Edge Case dimana harga awal adalah 0.
        Diskon berapapun pada harga 0 harus tetap menghasilkan 0.
        """
        # Act
        hasil = self.calc.hitung_diskon(0, 50)
        
        # Assert
        self.assertEqual(hasil, 0.0)

if __name__ == '__main__':
    unittest.main()