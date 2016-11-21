#kata: Latin SEO URL
# From a list of title
# Check allowed variants must match
# And generate a seo friendly url for each title 
import unittest
import pdb
from LatinUrlHelper import LatinUrlHelper

class TestLatinUrl(unittest.TestCase):
    dictionary = ["Castañas de Cajú", "Diseño gráfico", "McDonald's"]
    def setUp(self):
        self.helper = LatinUrlHelper(self.dictionary)

    def test_correcto(self):
        self.assertEqual(self.helper.match("Castañas de Cajú"), "Castañas de Cajú")
        self.assertEqual(self.helper.match("Diseño gráfico"), "Diseño gráfico")

    def test_castana_de_caju_maYUscULAs(self):
        self.assertEqual(self.helper.match("CasTAÑas de cAjú"), "Castañas de Cajú")
        self.assertEqual(self.helper.match("Diseño gráfIco"), "Diseño gráfico")

    def test_castana_de_caju_simple(self):
        self.assertEqual(self.helper.match("castanas de caju"), "Castañas de Cajú")
        self.assertEqual(self.helper.match("diseño grafico"), "Diseño gráfico")
   
    def test_castana_de_caju_todojunto(self):
        self.assertEqual(self.helper.match("CastañasdeCajú"), "Castañas de Cajú")
        self.assertEqual(self.helper.match("DiseñoGráfico"), "Diseño gráfico")
    
    def test_urls(self):
        self.assertEqual(self.helper.build_url("Castañas de Cajú"), "Castañas-de-Cajú")
        self.assertEqual(self.helper.build_url("Castañas de Cajú", to_ascii = True, lowercase=True, keep_char_at = [5]), "castañas-de-caju")
        self.assertEqual(self.helper.build_url("Diseño gráfico"), "Diseño-gráfico")
        self.assertEqual(self.helper.build_url("McDonald's"), "McDonalds")

if __name__ == '__main__':
    unittest.main()