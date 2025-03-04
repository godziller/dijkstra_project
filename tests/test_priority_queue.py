import unittest
from pq.priority_queue import PQBinaryHeap

class TestPQBinaryHeap(unittest.TestCase):

    def test_add_and_min(self):
        pq = PQBinaryHeap()
        
        # Add elements with varying keys
        pq.add(5, "A")
        pq.add(3, "B")
        pq.add(7, "C")
        
        # Test the min method
        key, value = pq.min()
        self.assertEqual(key, 3)
        self.assertEqual(value, "B")

    def test_remove_min(self):
        pq = PQBinaryHeap()
        
        pq.add(5, "A")
        pq.add(3, "B")
        pq.add(7, "C")
        
        # Test removing the min element
        key, value = pq.remove_min()
        self.assertEqual(key, 3)
        self.assertEqual(value, "B")
        
        # Now the min should be 5
        key, value = pq.min()
        self.assertEqual(key, 5)
        self.assertEqual(value, "A")

    def test_empty_queue(self):
        pq = PQBinaryHeap()
        
        # Test behavior on an empty queue
        key, value = pq.min()
        self.assertIsNone(key)
        self.assertIsNone(value)
        
        key, value = pq.remove_min()
        self.assertIsNone(key)
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()

