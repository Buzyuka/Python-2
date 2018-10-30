from unittest import TestCase

from .python1 import *


class Test(TestCase):
    def test_bubble_sort_forward(self):
        actual = bubble_sort([1, 2, 9, 0, 12, 55, 1, 0, 1, 7], lambda x, y: x > y)
        self.assertEqual([0, 0, 1, 1, 1, 2, 7, 9, 12, 55], actual)

    def test_bubble_sort_backward(self):
        actual = bubble_sort([1, 2, 9, 0, 12, 55, 1, 0, 1, 7], lambda x, y: x < y)
        self.assertEqual([55, 12, 9, 7, 2, 1, 1, 1, 0, 0], actual)

    def test_merge_sort(self):
        actual = merge_sort([1, 2, 9, 0, 12, 55, 1, 0, 1, 7])
        self.assertEqual([0, 0, 1, 1, 1, 2, 7, 9, 12, 55], actual)

    def test_select_median(self):
        arr = [1, 2, 9, 0, 12, 55, 1, 0, 1, 7]
        median = len(arr) // 2
        self.assertEqual(sorted(arr)[median], select(arr, median))

    def test_custom_select(self):
        arr = [1, 2, 9, 0, 12, 55, 1, 0, 1, 7]
        self.assertEqual(sorted(arr)[4], select(arr, 4))
