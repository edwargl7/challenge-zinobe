"""Unit Testing of Request Utilities"""

import unittest

from analytic.utils.requests_utils import request_get
from settings.settings import (HOST_REGION_API, TOKEN_REGION_API,
                               URL_REGION_API)


class TestRequestsUtil(unittest.TestCase):
    """Unit Testing of Request Utilities"""

    def test_valid_request_get(self):
        """Unit test with valid request to get"""
        url = URL_REGION_API + '/all'
        headers = {
            'x-rapidapi-key': TOKEN_REGION_API,
            'x-rapidapi-host': HOST_REGION_API
        }
        regions, error = request_get(url, headers)
        self.assertFalse(error)
        self.assertNotIn('error', regions)

    def test_invalid_request_get(self):
        """Unit test with invalid request to get"""
        url = URL_REGION_API + '/all'
        headers = None
        regions, error = request_get(url, headers)
        self.assertTrue(error)
        self.assertIn('msg', regions)
        self.assertIn('error', regions)


if __name__ == "__main__":
    unittest.main()
