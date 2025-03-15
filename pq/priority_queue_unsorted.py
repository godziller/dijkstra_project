class Element(object):
    def __init__(self, priority, item):
        self._priority = int(priority)
        self._element = item

    # O(1)
    def __gt__(self, other):
        if self._priority > other._priority:
            return True
        else:
            return False

    # O(1)
    def __lt__(self, other):
        if self._priority < other._priority:
            return True
        else:
            return False

class PriorityQueue(object):
    def __init__(self):
        self._list = list()
        self._length = 0

    # O(1)
    def add(self, priority, item):
        new_element = Element(priority, item)
        self._list.append(new_element)

    # O(n)
    def remove_min(self):
        if not self._list:
            return None
        min_index = 0
        for i in range(1, len(self._list)):
            if self._list[i] < self._list[min_index]:
                min_index = i
        # Swap the minimum element with the last element
        self._list[min_index], self._list[-1] = self._list[-1], self._list[min_index]
        # Pop the last element (which is the min) and return its value
        return self._list.pop()._element

    # O(n)
    def min(self):
        if not self._list:
            return None
        min_elem = self._list[0]
        for elem in self._list[1:]:
            if elem < min_elem:
                min_elem = elem
        return min_elem._element

    # O(1)
    def length(self):
        return len(self._list)
