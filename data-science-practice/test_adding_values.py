"""Tests demonstrating how to fill missing column values."""

import unittest

import pandas as pd


class TestAddingValues(unittest.TestCase):
    def test_fill_missing_values_with_the_average(self):
        people = pd.DataFrame({"score": [88, 92, None, 85]})

        # fillna replaces missing values. Here, we use the column average.
        average_score = people["score"].mean()
        people["score"] = people["score"].fillna(average_score)

        self.assertAlmostEqual(people.loc[2, "score"], (88 + 92 + 85) / 3)
        self.assertFalse(people["score"].isna().any())


if __name__ == "__main__":
    unittest.main(verbosity=2)
