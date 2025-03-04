

class PQBinaryHeap:
    """ Maintain an collection of items, popping by lowest key.

        This implementation maintains the collection using a binary heap.
        Uses an internally-defined class Element to store the items as a
        key (i.e. priority) and value (i.e. the actual item) pair.
        Use this class by typing PQBinaryHeap.Element() etc.
    """
    class Element:
        """ An element with a key and value. """
        
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            """ Return True if this key equals the other key. """
            return self._key == other._key

        def __lt__(self, other):
            """ Return True if this key is less than the other key. """
            return self._key < other._key

        def _wipe(self):
            """ Set the instance variables to None. """
            self._key = None
            self._value = None

    def __init__(self):
        """ Create a PQ with no elements. """

        # this is an array-based heap, so you need to create
        # an empty python list, and then maintain it
        # properly in the add and remove-min methods.
        self._heap = []
        self._size = 0
        
    def __str__(self):
        """ Return a breadth-first string of the values. """
        outstr = '['
        index = 0
        for elt in self._heap:
            outstr += str(index) \
                      + ':' + str(elt._value) \
                      + ':' + str(elt._key) + ','
            index += 1
        return outstr + ']'

    #
    # First, the four standard methods for the ADT

    def add(self, key, value):
        """ Add Element(key,value) to the heap. """
        e = PQBinaryHeap.Element(key, value)
        self._heap.append(e)
        self._upheap(self._size)
        self._size += 1
        return e

    def min(self):
        """ Return the min priority key,value. """
        if self._size:
            return self._heap[0]._key, self._heap[0]._value
        return None, None

    def remove_min(self):
        """ Remove and return the min priority key,value. """
        returnvalue = None
        returnkey = None
        if self._size > 0:
            returnkey = self._heap[0]._key
            returnvalue = self._heap[0]._value
            self._heap[0]._wipe()
            if self._size > 1: #if other items, restructure
                self._heap[0] = self._heap[-1]
                self._heap.pop()
                self._size -= 1
                self._downheap(0)
            else:
                self._heap.pop()
                self._size -= 1
        return returnkey, returnvalue

 
    def length(self):
        """ Return the number of items in the heap. """
        return self._size

    #
    # Now, the methods needed for the underlying heap implementation
    # These are designated 'private', with the leading underscore, since
    # client code should not have access to these - all access to the PQ
    # is meant to be via the standard 4 methods
    # You don't need to implement these if they are
    # not used in your 4 standard methods above, but
    # I find them useful.


    def _left(self, posn):
        """ Return the index of the left child of elt at index posn. """
        return 1 + 2*posn

    def _right(self, posn):
        """ Return the index of the right child of elt at index posn. """
        return 2 + 2*posn

    def _parent(self, posn):
        """ Return the index of the parent of elt at index posn. """
        return (posn - 1)//2
    
    def _upheap(self, posn):
        """ Bubble the item in posn in the heap up to its correct place. """
        if posn > 0 and self._upswap(posn, self._parent(posn)):
            self._upheap(self._parent(posn))

    def _upswap(self, posn, parent):
        """ If heap elt at posn has lower key than parent, swap. """
        if self._heap[posn] < self._heap[parent]:
            self._heap[posn], self._heap[parent] = self._heap[parent], self._heap[posn]
            self._heap[posn]._index = posn
            self._heap[parent]._index = parent
            return True
        return False

    def _downheap(self, posn):
        """ Bubble the item in posn in the heap down to its correct place. """
        #find minchild position
        #if minchild is in the heap
        #    if downswap with minchild is true
        #        downheap minchild
        minchild = self._left(posn)
        if minchild < self._size:
            if (minchild + 1 < self._size and
                self._heap[minchild]._key > self._heap[minchild + 1]._key):
                minchild +=1
            if self._downswap(posn, minchild):
                self._downheap(minchild)

    def _downswap(self, posn, child):
        """ If healp elt at posn has lower key than child, swap; else return False. """
        #Note: this could be merged with _upswap to provide a general
        #heapswap(first, second) method, which swaps if the element
        #first has lower key than the element second
        if self._heap[posn]._key > self._heap[child]._key:
            self._heap[posn], self._heap[child] = self._heap[child], self._heap[posn]
            self._heap[posn]._index = posn
            self._heap[child]._index = child
            return True
        return False

    def _printstructure(self):
        """ Print out the elements one to a line. """
        for elt in self._heap:
            if elt is not None:
                print('(', elt._key, ',', elt._value, ')')
            else:
                print('*')

    def _testadd():
        print('Testing that we can add items to an array-based binary heap PQ')
        pq = PQBinaryHeap()
        print('pq has size:', pq.length(), '(should be 0)')
        pq.add(25,'25')
        pq.add(4, '4')
        print('pq has size:', pq.length(), '(should be 2)')
        print(pq, '(should be 4,25, could also show index and value)')
        pq.add(19,'19')
        pq.add(12,'12')
        print(pq, '(should be 4,12,19,25)')
        pq.add(17,'17')
        pq.add(8,'8')
        print(pq, '(should be 4,12,8,25,17,19)')
        print('pq length:', pq.length(), '(should be 6)')
        print('pq min item:', pq.min(), '(should be 4)')
        print()
        return pq

    def _test():
        print('Testing that we can add and remove items from an array-based binary heap PQ')
        pq = PQBinaryHeap()
        print('pq has size:', pq.length())
        loc = {}
        print('Adding ant with value 25')
        loc['ant'] = pq.add(25,'ant')
        print('pq has size:', pq.length())
        print(pq)
        print('Adding bed with value 4')
        loc['bed'] = pq.add(4, 'bed')
        print(pq)
        print('Adding cat with value 14')
        loc['cat'] = pq.add(14,'cat')
        print(pq)
        print('Adding dog with value 12')
        loc['dog'] = pq.add(12,'dog')
        print(pq)
        print('Removing first')
        min = pq.remove_min()
        print("Just removed", str(min))
        print(pq)
        print('Adding egg with value 17')
        loc['egg'] = pq.add(17,'egg')
        print(pq)
        print('Adding fox with value 8')
        loc['fox'] = pq.add(8,'fox')
        print(pq)
        print('pq length:', pq.length())
        print('pq min item:', pq.min())
        for i in range(pq.length()):
            key, value = pq.remove_min()
            print('removed min (', key, value, '):', pq)

PQBinaryHeap._testadd()
PQBinaryHeap._test()
