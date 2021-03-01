"""Unit Testing of Country Metrics"""

from pandas import DataFrame
import unittest

from analytic.metrics.country_metrics import get_country_dataframe


class TestCountryMetrics(unittest.TestCase):
    """Unit Testing of Country Metrics"""

    def test_get_country_dataframe(self):
        """Unit test to get_country_dataframe"""
        df = get_country_dataframe()
        self.assertIsInstance(df, DataFrame)
        self.assertNotEqual(len(df), 0)


if __name__ == "__main__":
    unittest.main()
