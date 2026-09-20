"""Tests demonstrating label-based and position-based indexing."""

import unittest

import pandas as pd


class TestIndexing(unittest.TestCase):
    """Examples comparing label-based and position-based selection."""

    def setUp(self):
        """Create fresh sample data before each test method runs.

        The custom row labels make the difference between ``loc`` and ``iloc``
        easier to see.
        """
        self.people = pd.DataFrame(
            {
                "name": ["Ana", "Ben", "Cara"],
                "city": ["Toronto", "Montreal", "Vancouver"],
                "score": [88, 92, 90],
            },
            index=["person_a", "person_b", "person_c"],
        )

    def test_loc_selects_by_labels(self):
        """Show that loc selects data using row and column names.

        ``person_b`` is a row label and ``score`` is a column label, so this
        selects the value where that named row and column meet.
        """
        # .loc uses row and column labels.
        value = self.people.loc["person_b", "score"]

        self.assertEqual(value, 92)

    def test_iloc_selects_by_positions(self):
        """Show that iloc selects data using integer positions.

        ``0:2`` selects the first two rows, while ``0`` selects the first
        column. The end of a positional slice is not included.
        """
        # .iloc uses zero-based row and column positions.
        first_two_names = self.people.iloc[0:2, 0]

        self.assertEqual(first_two_names.tolist(), ["Ana", "Ben"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
