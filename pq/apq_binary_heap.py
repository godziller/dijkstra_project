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

class APQBinaryHeap(object):
    def __init__(self):
        # O(1)
        self._data = []  # binary heap stored as a list

    # O(log n) average-case
    def add(self, key, item):
        """
        add(key, item)
        Add a new item into the priority queue with priority key,
        and return its Element in the APQ.
        """
        index = len(self._data)
        element = Element(key, item, index)
        self._data.append(element)
        self._bubble_up(index)
        return element

    # O(log n)
    def _bubble_up(self, index):
        """
        Bubble up the element at index to restore heap order.
        """
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index]._key < self._data[parent]._key:
                self._swap(index, parent)
                index = parent
            else:
                break

    # O(log n)
    def _bubble_down(self, index):
        """
        Bubble down the element at index to restore heap order.
        """
        n = len(self._data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < n and self._data[left]._key < self._data[smallest]._key:
                smallest = left
            if right < n and self._data[right]._key < self._data[smallest]._key:
                smallest = right
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    # O(1)
    def _swap(self, i, j):
        """
        Swap the elements at indices i and j and update their indices.
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._data[i]._index = i
        self._data[j]._index = j

    # O(1)
    def min(self):
        """
        min()
        Return the value with the minimum key.
        """
        if not self._data:
            return None
        return self._data[0]._value

    # O(log n)
    def remove_min(self):
        """
        remove_min()
        Remove and return the value with the minimum key.
        """
        if not self._data:
            return None
        self._swap(0, len(self._data) - 1)
        removed = self._data.pop()  # O(1) removal from the end
        value = removed._value     # store value before wiping
        removed._wipe()            # O(1)
        if self._data:
            self._bubble_down(0)
        return value

    # O(1)
    def length(self):
        """
        length()
        Return the number of items in the priority queue.
        """
        return len(self._data)

    # O(log n) worst-case
    def update_key(self, element, newkey):
        """
        update_key(element, newkey)
        Update the key in element to be newkey, and rebalance the APQ.
        """
        oldkey = element._key
        element._key = newkey
        index = element._index
        if newkey < oldkey:
            self._bubble_up(index)
        else:
            self._bubble_down(index)

    # O(1)
    def get_key(self, element):
        """
        get_key(element)
        Return the current key for element.
        """
        return element._key

    # O(log n) worst-case
    def remove(self, element):
        """
        remove(element)
        Remove and return the (key, value) pair for this element,
        and rebalance the APQ.
        """
        index = element._index
        if index == len(self._data) - 1:
            removed = self._data.pop()
        else:
            self._swap(index, len(self._data) - 1)
            removed = self._data.pop()
            if index < len(self._data):
                self._bubble_up(index)
                self._bubble_down(index)
        key, value = removed._key, removed._value
        removed._wipe()
        return (key, value)
