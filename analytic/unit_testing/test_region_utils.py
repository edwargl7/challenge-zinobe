"""Unit Testing of Region Utilities"""

import unittest

from analytic.utils.region_utils import (get_country_by_region,
                                         get_regions)


class TestRegionUtil(unittest.TestCase):
    """Unit Testing of Region Utilities"""

    def test_get_regions(self):
        """Unit test to get_regions"""
        regions, error = get_regions()
        self.assertFalse(error)
        self.assertIn('regions', regions)
        self.assertNotIn('error', regions)

    def test_valid_get_country_by_region(self):
        """Unit test to get_country_by_region, positive response"""
        country, error = get_country_by_region('Africa')
        self.assertFalse(error)
        self.assertIn('country', country)
        self.assertNotIn('error', country)

    def test_invalid_get_country_by_region(self):
        """Unit test to get_country_by_region, negative response"""
        country, error = get_country_by_region('xyz')
        self.assertTrue(error)
        self.assertIn('msg', country)
        self.assertIn('error', country)


if __name__ == "__main__":
    unittest.main()
