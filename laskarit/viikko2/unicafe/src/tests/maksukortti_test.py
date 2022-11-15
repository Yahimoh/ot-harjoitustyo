import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa: 10.00 euroa")

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa: 11.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa: 5.00 euroa")

    def test_rahan_ottaminen_ei_toimi_jos_saldoa_ei_riittavasti(self):
        kortti = Maksukortti(100)
        kortti.ota_rahaa(150)

        self.assertEqual(str(kortti), "Kortilla on rahaa: 1.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        toimiko = self.maksukortti.ota_rahaa(500)

        self.assertEqual(toimiko, True)

    def test_rahan_ottaminen_ei_toimi(self):
        toimiko = self.maksukortti.ota_rahaa(1100)

        self.assertEqual(toimiko, False)
