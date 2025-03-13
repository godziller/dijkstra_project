import unittest
from pq.apq_binary_heap import APQBinaryHeap


# Unit tests for APQHeap
class TestAPQHeap(unittest.TestCase):
    def setUp(self):
        # O(1): Create a new APQHeap instance before each test.
        self.apq = APQBinaryHeap()

    # O(1)
    def test_add_and_length(self):
        # Initially, length should be 0.
        self.assertEqual(self.apq.length(), 0)
        # Add elements.
        self.apq.add(10, "a")
        self.apq.add(5, "b")
        self.apq.add(15, "c")
        self.assertEqual(self.apq.length(), 3)

    # O(1)
    def test_min(self):
        # min should be None for an empty heap.
        self.assertIsNone(self.apq.min())
        self.apq.add(10, "a")
        self.apq.add(5, "b")
        self.apq.add(15, "c")
        # min should return the element with the lowest key ("b").
        self.assertEqual(self.apq.min(), "b")

    # O(log n)
    def test_remove_min(self):
        self.apq.add(10, "a")
        self.apq.add(5, "b")
        self.apq.add(15, "c")
        removed_value = self.apq.remove_min()
        self.assertEqual(removed_value, "b")
        self.assertEqual(self.apq.length(), 2)
        self.assertEqual(self.apq.min(), "a")

    # O(log n)
    def test_update_key_and_get_key(self):
        element = self.apq.add(10, "a")
        self.assertEqual(self.apq.get_key(element), 10)
        self.apq.update_key(element, 2)
        self.assertEqual(self.apq.get_key(element), 2)
        self.apq.add(5, "b")
        self.assertEqual(self.apq.min(), "a")

    # O(log n)
    def test_remove_element(self):
        e1 = self.apq.add(10, "a")
        e2 = self.apq.add(5, "b")
        e3 = self.apq.add(15, "c")
        removed = self.apq.remove(e1)
        self.assertEqual(removed, (10, "a"))
        self.assertEqual(self.apq.length(), 2)
        keys = [self.apq.get_key(e) for e in self.apq._data]
        self.assertIn(5, keys)
        self.assertIn(15, keys)

    # O(1)
    def test_remove_from_empty(self):
        # For an empty heap, min() and remove_min() should return None.
        self.assertIsNone(self.apq.min())
        self.assertIsNone(self.apq.remove_min())

if __name__ == '__main__':
    unittest.main()
