"""Tests demonstrating pandas Series basics."""

import unittest

import pandas as pd


class TestSeries(unittest.TestCase):
    def test_create_a_series(self):
        # A Series is a single labelled column of data.
        temperatures = pd.Series([20, 22, 19], name="temperature")

        self.assertEqual(temperatures.name, "temperature")
        self.assertEqual(temperatures.tolist(), [20, 22, 19])


if __name__ == "__main__":
    unittest.main(verbosity=2)
