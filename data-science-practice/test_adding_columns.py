"""Tests demonstrating how to add columns to a pandas DataFrame."""

import unittest

import pandas as pd


class TestAddingColumns(unittest.TestCase):
    def test_add_a_calculated_column(self):
        people = pd.DataFrame({"name": ["Ana", "Ben"], "age": [24, 31]})

        # Calculations on a column operate on every row.
        people["age_next_year"] = people["age"] + 1

        self.assertEqual(people["age_next_year"].tolist(), [25, 32])


if __name__ == "__main__":
    unittest.main(verbosity=2)
