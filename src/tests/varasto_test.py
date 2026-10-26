import unittest
from varasto import Varasto
import varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # My tests 

    def test_negative_values_corrected_in_constructor(self):
        varasto = Varasto(-1.0, -1.0)
        # Break test here
        self.assertAlmostEqual(varasto.saldo, 1.0)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_clamp_to_volume_in_constructor(self):
        varasto = Varasto(0.5, 1.0)
        self.assertAlmostEqual(varasto.saldo, 0.5)
        self.assertAlmostEqual(varasto.tilavuus, 0.5)

    def test_ignore_negative_values_on_add(self):
        current_saldo = self.varasto.saldo
        self.varasto.add(-1.0)
        self.assertAlmostEqual(self.varasto.saldo, current_saldo)

    def test_clamp_to_volume_on_add(self):
        current_volume = self.varasto.tilavuus
        self.varasto.add(100.0)
        self.assertAlmostEqual(self.varasto.saldo, current_volume)

    def test_return_zero_for_negative_values_on_get(self):
        actual_value = self.varasto.get(-1.0)
        self.assertAlmostEqual(actual_value, 0.0)

    def test_clamp_to_saldo_on_get(self):
        expected_value = self.varasto.saldo
        actual_value = self.varasto.get(100.0)
        self.assertAlmostEqual(actual_value, expected_value)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
    def test_string_output(self):
        actual_str = str(self.varasto)
        expected_str = "saldo = 0.0, vielä tilaa 10.0"
        self.assertEqual(actual_str, expected_str)
