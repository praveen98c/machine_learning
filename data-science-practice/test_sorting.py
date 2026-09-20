"""Tests demonstrating how to sort pandas rows."""

import unittest

import pandas as pd


class TestSorting(unittest.TestCase):
    def test_sort_rows_by_a_column(self):
        people = pd.DataFrame(
            {"name": ["Ana", "Ben", "Cara", "Dan"], "age": [24, 31, 29, 31]}
        )

        sorted_people = people.sort_values("age")

        self.assertEqual(sorted_people["name"].tolist(), ["Ana", "Cara", "Ben", "Dan"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
