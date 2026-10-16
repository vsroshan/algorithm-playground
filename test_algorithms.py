import random
import unittest

from mail import (
    binary_search,
    bubble_sort,
    linear_search,
    merge_sort,
    selection_sort,
)


class TestSearchingAlgorithms(unittest.TestCase):
    def test_linear_search_finds_target(self):
        values = [12, 31, 44, 57, 73, 88]
        index, comparisons = linear_search(values, 73)
        self.assertEqual(values[index], 73)
        self.assertEqual(comparisons, 5)

    def test_linear_search_missing_target(self):
        index, comparisons = linear_search([10, 20, 30], 99)
        self.assertIsNone(index)
        self.assertEqual(comparisons, 3)

    def test_binary_search_finds_target(self):
        values = [12, 31, 44, 57, 73, 88]
        index, comparisons = binary_search(values, 73)
        self.assertIsNotNone(index)
        self.assertEqual(values[index], 73)
        self.assertGreater(comparisons, 0)

    def test_binary_search_missing_target(self):
        index, comparisons = binary_search([10, 20, 30], 99)
        self.assertIsNone(index)
        self.assertGreater(comparisons, 0)


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.values = [64, 25, 12, 22, 11]
        self.expected = [11, 12, 22, 25, 64]

    def test_bubble_sort(self):
        result, comparisons = bubble_sort(self.values)
        self.assertEqual(result, self.expected)
        self.assertGreater(comparisons, 0)

    def test_selection_sort(self):
        result, comparisons = selection_sort(self.values)
        self.assertEqual(result, self.expected)
        self.assertGreater(comparisons, 0)

    def test_merge_sort(self):
        result, comparisons = merge_sort(self.values)
        self.assertEqual(result, self.expected)
        self.assertGreater(comparisons, 0)

    def test_empty_lists(self):
        self.assertEqual(bubble_sort([])[0], [])
        self.assertEqual(selection_sort([])[0], [])
        self.assertEqual(merge_sort([])[0], [])

    def test_single_element_lists(self):
        self.assertEqual(bubble_sort([42])[0], [42])
        self.assertEqual(selection_sort([42])[0], [42])
        self.assertEqual(merge_sort([42])[0], [42])

    def test_duplicate_values(self):
        values = [5, 2, 5, 1, 2]
        expected = [1, 2, 2, 5, 5]
        self.assertEqual(bubble_sort(values)[0], expected)
        self.assertEqual(selection_sort(values)[0], expected)
        self.assertEqual(merge_sort(values)[0], expected)

    def test_random_datasets(self):
        random.seed(42)
        for size in [0, 1, 10, 100]:
            values = [
                random.randint(0, 1000)
                for _ in range(size)
            ]
            expected = sorted(values)
            self.assertEqual(bubble_sort(values)[0], expected)
            self.assertEqual(selection_sort(values)[0], expected)
            self.assertEqual(merge_sort(values)[0], expected)


if __name__ == "__main__":
    unittest.main()
