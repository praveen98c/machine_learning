"""Tests demonstrating how to filter pandas rows."""

import unittest

import pandas as pd


class TestFiltering(unittest.TestCase):
    def setUp(self):
        self.people = pd.DataFrame(
            {
                "name": ["Ana", "Ben", "Cara", "Dan"],
                "age": [24, 31, 29, 31],
                "score": [88, 92, None, 85],
            }
        )

    def test_filter_with_one_condition(self):
        # A Boolean condition keeps only rows where the condition is True.
        people_over_25 = self.people[self.people["age"] > 25]

        self.assertEqual(people_over_25["name"].tolist(), ["Ben", "Cara", "Dan"])

    def test_filter_with_a_boolean_mask(self):
        # Put each condition in parentheses and combine them with & (AND).
        mask = (
            (self.people["age"] >= 25)
            & (self.people["age"] <= 31)
            & (self.people["score"] >= 90)
        )

        matching_people = self.people.loc[mask].copy()

        self.assertEqual(mask.tolist(), [False, True, False, False])
        self.assertEqual(matching_people["name"].tolist(), ["Ben"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
