"""Tests demonstrating how to select a subset of DataFrame columns."""

import unittest

import pandas as pd


class TestSelectingSubsetOfColumns(unittest.TestCase):
    def test_select_multiple_columns(self):
        people = pd.DataFrame(
            {
                "name": ["Ana", "Ben", "Cara"],
                "age": [24, 31, 29],
                "city": ["Toronto", "Montreal", "Toronto"],
                "score": [88, 92, 90],
            }
        )

        # Pass a list of column names to select a smaller DataFrame.
        # The order in the list determines the order in the result.
        contact_view = people[["name", "city"]]

        self.assertEqual(contact_view.columns.tolist(), ["name", "city"])
        self.assertEqual(
            contact_view.to_dict(orient="records"),
            [
                {"name": "Ana", "city": "Toronto"},
                {"name": "Ben", "city": "Montreal"},
                {"name": "Cara", "city": "Toronto"},
            ],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
