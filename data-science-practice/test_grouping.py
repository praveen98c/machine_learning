"""Tests demonstrating how to group and summarize pandas data."""

import unittest

import pandas as pd


class TestGrouping(unittest.TestCase):
    def test_group_and_find_the_average(self):
        people = pd.DataFrame(
            {
                "city": ["Toronto", "Montreal", "Toronto", "Montreal"],
                "age": [24, 31, 29, 31],
            }
        )

        average_age_by_city = people.groupby("city")["age"].mean()

        self.assertEqual(average_age_by_city["Montreal"], 31)
        self.assertEqual(average_age_by_city["Toronto"], 26.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
