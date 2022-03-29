import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()

    def test_luotu_kassapaate_oikein(self):
        self.assertEqual(str(self.paate), "Kassassa rahaa: 1000.0, edullisia myyty: 0, maukkaita myyty: 0")

    def test_edullisen_osto_toimii(self):
        vaihtorahat = self.paate.syo_edullisesti_kateisella(240)

        self.assertEqual(vaihtorahat, 0)

    def test_maukas_osto_toimii(self):
        vaihtorahat = self.paate.syo_maukkaasti_kateisella(400)

        self.assertEqual(vaihtorahat, 0)

    def test_edullisen_osto_ei_toimi(self):
        vaihtorahat = self.paate.syo_edullisesti_kateisella(230)

        self.assertEqual(vaihtorahat, 230)

    def test_maukas_osto_toimii(self):
        vaihtorahat = self.paate.syo_maukkaasti_kateisella(390)

        self.assertEqual(vaihtorahat, 390)
