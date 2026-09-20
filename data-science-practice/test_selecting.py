"""Tests demonstrating how to select pandas columns."""

import unittest

import pandas as pd


class TestSelecting(unittest.TestCase):
    def test_select_a_column(self):
        people = pd.DataFrame({"name": ["Ana", "Ben", "Cara", "Dan"]})

        # Square brackets select a column and return a Series.
        names = people["name"]

        self.assertEqual(names.tolist(), ["Ana", "Ben", "Cara", "Dan"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
