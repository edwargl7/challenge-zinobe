"""Unit Testing of Country Utilities"""

import unittest

from analytic.utils.country_utils import (get_country_language_name,
                                          get_country_name)


class TestCountryUtil(unittest.TestCase):
    """Unit Testing of Country Utilities"""

    def test_valid_get_country_language_name(self):
        """Unit test to get_country_language_name, positive response"""
        country_json = {"languages": [
            {"iso639_1": "en",
             "iso639_2": "eng",
             "name": "English",
             "nativeName": "English"}]
        }
        language, error = get_country_language_name(country_json)
        self.assertFalse(error)
        self.assertIn('language_name', language)
        self.assertNotIn('error', language)

    def test_invalid_get_country_language_name(self):
        """Unit test to get_country_language_name, negative response"""
        country_json = {}
        language, error = get_country_language_name(country_json)
        self.assertTrue(error)
        self.assertIn('msg', language)
        self.assertIn('error', language)

    def test_valid_get_country_name(self):
        """Unit test to get_country_name, positive response"""
        country_json = {"name": "Anguilla"}
        country_name, error = get_country_name(country_json)
        self.assertFalse(error)
        self.assertIn('country_name', country_name)
        self.assertNotIn('error', country_name)

    def test_invalid_get_country_name(self):
        """Unit test to get_country_name, negative response"""
        country_json = {}
        country_name, error = get_country_name(country_json)
        self.assertTrue(error)
        self.assertIn('msg', country_name)
        self.assertIn('error', country_name)


if __name__ == "__main__":
    unittest.main()
