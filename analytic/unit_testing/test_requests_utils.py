"""Unit Testing of Request Utilities"""

import unittest

from analytic.utils.region_utils import get_regions


class TestRequestsUtil(unittest.TestCase):
    """Unit Testing of Region Utilities"""

    def test_get_regions(self):
        """Unit test valid get_regions"""
        regions, error = get_regions()
        self.assertFalse(error)
        self.assertIn('regions', regions)
        self.assertNotIn('error', regions)


if __name__ == "__main__":
    unittest.main()
