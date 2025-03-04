import unittest
from pq.apq_unsorted_list import APQUnsortedList

class TestAPQUnsortedList(unittest.TestCase):

    def setUp(self):
        # O(1): Create a new APQUnsortedList instance before each test.
        self.apq = APQUnsortedList()

    # O(1)
    def test_add_and_length(self):
        # Initially, the queue should be empty.
        self.assertEqual(self.apq.length(), 0)
        # O(1): Add three elements.
        self.apq.add(10, "a")
        self.apq.add(5, "b")
        self.apq.add(15, "c")
        # O(1): Check that length is updated correctly.
        self.assertEqual(self.apq.length(), 3)

    # O(n)
    def test_min(self):
        # O(n): Test that min on an empty APQ returns None.
        self.assertIsNone(self.apq.min())
        # Add elements.
        self.apq.add(10, "a")
        self.apq.add(5, "b")
        self.apq.add(15, "c")
        # O(n): Check that min returns the value with the lowest key ("b").
        self.assertEqual(self.apq.min(), "b")

    # O(n)
    def test_remove_min(self):
        # Add elements.
        self.apq.add(10, "a")
        self.apq.add(5, "b")
        self.apq.add(15, "c")
        # O(n): remove_min should return the value with the smallest key ("b").
        removed_value = self.apq.remove_min()
        self.assertEqual(removed_value, "b")
        # O(1): Check that length and min update accordingly.
        self.assertEqual(self.apq.length(), 2)
        self.assertEqual(self.apq.min(), "a")

    # O(1)
    def test_update_key_and_get_key(self):
        # Add an element and check its key.
        element = self.apq.add(10, "a")
        self.assertEqual(self.apq.get_key(element), 10)
        # O(1): Update the key and verify the change.
        self.apq.update_key(element, 2)
        self.assertEqual(self.apq.get_key(element), 2)
        # Add another element.
        self.apq.add(5, "b")
        # Now, min should be "a" because its key is 2.
        self.assertEqual(self.apq.min(), "a")

    # O(1)
    def test_remove_element(self):
        # Add multiple elements.
        e1 = self.apq.add(10, "a")
        e2 = self.apq.add(5, "b")
        e3 = self.apq.add(15, "c")
        # O(1): Remove a specific element (e1).
        removed = self.apq.remove(e1)
        self.assertEqual(removed, (10, "a"))
        self.assertEqual(self.apq.length(), 2)
        # O(1): Check that the remaining elements have the expected keys.
        keys = [self.apq.get_key(e) for e in self.apq._data]
        self.assertIn(5, keys)
        self.assertIn(15, keys)

    # O(n)
    def test_remove_from_empty(self):
        # O(n): Ensure that operations on an empty APQ return None gracefully.
        self.assertIsNone(self.apq.min())
        self.assertIsNone(self.apq.remove_min())

if __name__ == '__main__':
    unittest.main()
