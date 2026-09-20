"""Tests demonstrating how to combine related DataFrames."""

import unittest

import pandas as pd


class TestMerging(unittest.TestCase):
    def test_merge_tables_using_a_shared_column(self):
        orders = pd.DataFrame(
            {"order_id": [101, 102, 103], "customer_id": [1, 2, 1]}
        )
        customers = pd.DataFrame(
            {"customer_id": [1, 2], "customer_name": ["Ana", "Ben"]}
        )

        # merge() matches rows using the shared customer_id column.
        order_details = orders.merge(customers, on="customer_id", how="left")

        self.assertEqual(order_details["customer_name"].tolist(), ["Ana", "Ben", "Ana"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
