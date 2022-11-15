import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luotu_kassapaate_oikein_kateisella(self):
        self.assertEqual(str(self.paate), "Kassassa rahaa: 1000.0, edullisia myyty: 0, maukkaita myyty: 0")

    def test_edullisen_osto_toimii_kateisella(self):
        vaihtorahat = self.paate.syo_edullisesti_kateisella(240)

        self.assertEqual(vaihtorahat, 0)

    def test_maukas_osto_toimii(self):
        vaihtorahat = self.paate.syo_maukkaasti_kateisella(400)

        self.assertEqual(vaihtorahat, 0)

    def test_edullisen_osto_ei_toimi_kateisella(self):
        vaihtorahat = self.paate.syo_edullisesti_kateisella(230)

        self.assertEqual(vaihtorahat, 230)

    def test_maukas_osto_ei_toimi_kateisella(self):
        vaihtorahat = self.paate.syo_maukkaasti_kateisella(390)

        self.assertEqual(vaihtorahat, 390)

    def test_edullisen_osto_toimii_kortilla(self):
        toteutus = self.paate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(True, toteutus)

    def test_maukas_osto_toimii_kortilla(self):
        toteutus = self.paate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(True, toteutus)

    def test_edullisen_osto_ei_toimi_kortilla(self):
        broke_kortti = Maksukortti(100)
        toteutus = self.paate.syo_edullisesti_kortilla(broke_kortti)

        self.assertEqual(False, toteutus)

    def test_maukas_osto_ei_toimi_kortilla(self):
        broke_kortti = Maksukortti(100)
        toteutus = self.paate.syo_maukkaasti_kortilla(broke_kortti)

        self.assertEqual(False, toteutus)

    def test_kortille_rahan_lataus_toimii(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa: 15.00 euroa")

    def test_kortille_rahan_lataus_ei_toimi(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -5)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa: 10.00 euroa")


	
