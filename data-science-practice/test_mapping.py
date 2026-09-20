"""Tests demonstrating how to transform Series values with map()."""

import unittest

import pandas as pd


class TestMapping(unittest.TestCase):
    def test_map_values_with_a_dictionary(self):
        products = pd.DataFrame(
            {"product": ["Laptop", "Mouse", "Desk"], "category_code": ["E", "E", "F"]}
        )
        category_names = {"E": "Electronics", "F": "Furniture"}

        # map() looks up every category code in the dictionary.
        products["category"] = products["category_code"].map(category_names)

        self.assertEqual(
            products["category"].tolist(),
            ["Electronics", "Electronics", "Furniture"],
        )

    def test_map_values_with_a_function(self):
        names = pd.Series(["ana", "BEN", "cara"])

        # A function passed to map() is called once for each value.
        display_names = names.map(str.title)

        self.assertEqual(display_names.tolist(), ["Ana", "Ben", "Cara"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
