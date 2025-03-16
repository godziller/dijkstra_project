class Element:
    """A key, value and index."""
    def __init__(self, k, v, i):
        # O(1)
        self._key = k
        self._value = v
        self._index = i

    # O(1)
    def __eq__(self, other):
        return self._key == other._key

    # O(1)
    def __lt__(self, other):
        return self._key < other._key

    # O(1)
    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None


class APQUnsortedList(object):
    def __init__(self):
        # O(1)
        self._data = []  # unsorted list to store the elements

    # O(1)
    def add(self, key, item):
        """
        add(key, item)
        Add a new item into the priority queue with priority key,
        and return its Element in the APQ.
        """
        index = len(self._data)
        element = Element(key, item, index)
        self._data.append(element)
        return element

    # O(n)
    def min(self):
        """
        min()
        Return the value with the minimum key.
        """
        if not self._data:
            return None
        min_elem = self._data[0]
        for elem in self._data[1:]:
            if elem._key < min_elem._key:
                min_elem = elem
        return min_elem._value

    # O(n)
    def remove_min(self):
        """
        remove_min()
        Remove and return the value with the minimum key.
        O(n)
        """
        if not self._data:
            return None
        min_index = 0
        # This loop is the O(N) inducing part of remove_min
        for i in range(1, len(self._data)):     # The O(n) culprit
            if self._data[i]._key < self._data[min_index]._key:
                min_index = i
        # Swap the minimum element with the last element
        self._data[min_index], self._data[-1] = self._data[-1], self._data[min_index]
        self._data[min_index]._index = min_index  # update the swapped element's index
        removed = self._data.pop()  # O(1) removal from the end
        value = removed._value  # store value before wiping, if I don't I loose the value
        removed._wipe()  # O(1)
        return value

    # O(1)
    def length(self):
        """
        length()
        Return the number of items in the priority queue.
        """
        return len(self._data)

    # O(1)
    def update_key(self, element, newkey):
        """
        update_key(element, newkey)
        Update the key in element to be newkey, and rebalance the APQ.
        For an unsorted list, no reordering is necessary.
        """
        element._key = newkey

    # O(1)
    def get_key(self, element):
        """
        get_key(element)
        Return the current key for element.
        """
        return element._key

    # O(1)
    def remove(self, element):
        """
        remove(element)
        Remove and return the (key, value) pair for this element,
        and rebalance the APQ.
        """
        index = element._index
        if index != len(self._data) - 1:
            # Swap the element with the last element for efficient removal.
            self._data[index], self._data[-1] = self._data[-1], self._data[index]
            self._data[index]._index = index  # update the swapped element's index
        removed = self._data.pop()  # O(1)
        key, value = removed._key, removed._value
        removed._wipe()  # O(1)
        return (key, value)