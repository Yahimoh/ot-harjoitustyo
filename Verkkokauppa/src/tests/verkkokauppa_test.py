import unittest
from verkkokauppa import Verkkokauppa

class TestVerkkokauppa(unittest.TestCase):
    def setUp(self):
        self.kauppa = Verkkokauppa("asiakas")

    def test_konstruktori_asettaa_kayttajan_nakyman_oikein_asiakkaalle(self):
        self.assertEqual("Asiakkaan näkymä", str(self.kauppa))