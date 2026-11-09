import unittest

from main import (
    hitung_ipk,
    validasi_nim,
    konversi_nilai_huruf
)


class TestHitungIPK(unittest.TestCase):

    def test_ipk_normal(self):
        self.assertEqual(
            hitung_ipk([(4.0, 3), (3.0, 2)]),
            3.6
        )

    def test_ipk_kosong(self):
        with self.assertRaises(ValueError):
            hitung_ipk([])

    def test_ipk_sks_nol(self):
        with self.assertRaises(ValueError):
            hitung_ipk([(4.0, 0)])


class TestValidasiNIM(unittest.TestCase):

    def test_nim_valid(self):
        self.assertTrue(validasi_nim("2026000001"))

    def test_nim_tidak_valid(self):
        self.assertFalse(validasi_nim("12345"))

    def test_nim_mengandung_huruf(self):
        self.assertFalse(validasi_nim("2026ABC001"))


class TestKonversiNilai(unittest.TestCase):

    def test_nilai_a(self):
        self.assertEqual(konversi_nilai_huruf(90), "A")

    def test_nilai_b_plus(self):
        self.assertEqual(konversi_nilai_huruf(80), "B+")

    def test_nilai_e(self):
        self.assertEqual(konversi_nilai_huruf(40), "E")

    def test_nilai_invalid(self):
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(110)


if __name__ == "__main__":
    unittest.main()