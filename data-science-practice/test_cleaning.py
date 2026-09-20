"""Tests demonstrating common pandas data-cleaning operations."""

import unittest

import pandas as pd


class TestCleaning(unittest.TestCase):
    def test_remove_duplicate_rows(self):
        names = pd.DataFrame({"name": ["Ana", "Ben", "Ana"]})

        unique_names = names.drop_duplicates()

        self.assertEqual(unique_names["name"].tolist(), ["Ana", "Ben"])

    def test_remove_rows_with_missing_required_values(self):
        people = pd.DataFrame(
            {"name": ["Ana", "Ben", "Cara"], "email": ["a@example.com", None, "c@example.com"]}
        )

        # subset limits the missing-value check to required columns.
        people_with_email = people.dropna(subset=["email"])

        self.assertEqual(people_with_email["name"].tolist(), ["Ana", "Cara"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
