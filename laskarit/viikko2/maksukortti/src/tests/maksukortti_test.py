import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.5 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

    def test_negatiivisen_saldon_lataaminen_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-5)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_kortilla_pystyy_ostaa_edullisen_lounaan_kun_saldo_on_tasan(self):
        tasanEdullinenKortti = Maksukortti(2.5)
        tasanEdullinenKortti.syo_edullisesti()

        self.assertEqual(str(tasanEdullinenKortti), "Kortilla on rahaa 0.0 euroa")

    def test_kortilla_pystyy_ostaa_maukkaan_lounaan_kun_saldo_on_tasan(self):
        tasanMaukasKortti = Maksukortti(4)
        tasanMaukasKortti.syo_maukkaasti()

        self.assertEqual(str(tasanMaukasKortti), "Kortilla on rahaa 0 euroa")

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_rahan_lataaminen_toimii(self):
        self.kortti.lataa_rahaa(110)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 120 euroa")

    def test_rahan_ottaminen_toimii(self):
        onnistuminen = self.kortti.ota_rahaa(5)
        self.assertEqual(True, onnistuminen)

    def test_rahan_ottaminen_ei_toimi(self):
        onnistuminen = self.kortti.ota_rahaa(11)
        self.assertEqual(False, onnistuminen)
