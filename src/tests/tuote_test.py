import unittest
from entities.tuote import Tuote


class TestTuote(unittest.TestCase):
    def setUp(self):
        self.tuote = Tuote("Mango", 2.99)

    def test_luotu_tuote_oikein(self):
        self.assertEqual(str(self.tuote), "Mango: 2.99€")

    def test_get_nimi(self):
        self.assertEqual(self.tuote.get_nimi(), "Mango")

    def test_get_hinta(self):
        self.assertEqual(self.tuote.get_hinta(), 2.99)

    def test_update_nimi(self):
        self.tuote.update_nimi("Vadelma")
        self.assertEqual(self.tuote.get_nimi(), "Vadelma")

    def test_update_hinta(self):
        self.tuote.update_hinta(3.49)
        self.assertEqual(self.tuote.get_hinta(), 3.49)
