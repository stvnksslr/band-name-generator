from unittest import TestCase

from app.band_name_generator import get_band_name


class BandNameGeneratorTest(TestCase):

    def test__check_band_name_generator_returns_a_string(self):
        band_name = get_band_name(optional_word="mike")
        self.assertTrue(band_name)
