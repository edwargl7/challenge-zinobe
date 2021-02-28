"""Unit Testing of Region Utilities"""

import unittest

from analytic.utils.region_utils import get_regions
from settings.settings import (HOST_REGION_API, TOKEN_REGION_API,
                               URL_REGION_API)


class TestRegionUtil(unittest.TestCase):
    """Unit Testing of Region Utilities"""

    def test_valid_request_get_regions(self):
        """Unit test with valid request to get_regions"""
        url = URL_REGION_API + '/all'
        headers = {
            'x-rapidapi-key': TOKEN_REGION_API,
            'x-rapidapi-host': HOST_REGION_API
        }
        regions, error = get_regions(url, headers)
        self.assertFalse(error)
        self.assertNotIn('error', regions)

    def test_invalid_request_get_regions(self):
        """Unit test with invalid request to get_regions"""
        url = URL_REGION_API + '/all'
        headers = None
        regions, error = get_regions(url, headers)
        self.assertTrue(error)
        self.assertIn('msg', regions)
        self.assertIn('error', regions)


if __name__ == "__main__":
    unittest.main()
