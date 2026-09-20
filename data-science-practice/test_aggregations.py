"""Tests demonstrating how to summarize pandas data."""

import unittest

import pandas as pd


class TestAggregations(unittest.TestCase):
    def test_calculate_multiple_summaries(self):
        scores = pd.Series([80, 90, 100], name="score")

        # agg() calculates several summaries in one operation.
        summary = scores.agg(["min", "max", "mean"])

        self.assertEqual(summary["min"], 80)
        self.assertEqual(summary["max"], 100)
        self.assertEqual(summary["mean"], 90)

    def test_count_unique_values(self):
        cities = pd.Series(["Toronto", "Montreal", "Toronto", "Toronto"])

        counts = cities.value_counts()

        self.assertEqual(counts["Toronto"], 3)
        self.assertEqual(counts["Montreal"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
