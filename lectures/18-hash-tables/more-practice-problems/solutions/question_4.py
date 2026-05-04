from random import randrange
from ctypes import py_object
from UnsortedArrayMap import UnsortedArrayMap
from DoublyLinkedList import DoublyLinkedList


def make_array(n):
    return (n * py_object)()


class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = randrange(1, self.p - 1)
            self.b = randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N

    def __init__(self, N=64):
        self.table = make_array(N)
        for i in range(N):
            self.table[i] = UnsortedArrayMap()
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)
        self.order = DoublyLinkedList()  # keys in insertion order

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        i = self.h(key)
        value, _ = self.table[i][key]  # bucket stores (value, dll_node)
        return value

    def __setitem__(self, key, value):
        i = self.h(key)
        curr_bucket = self.table[i]

        try:
            _, node = curr_bucket[key]             # key already exists
            curr_bucket[key] = (value, node)      # update value, keep same dll node
        except KeyError:
            node = self.order.add_last(key)       # new key: append to FIFO order
            curr_bucket[key] = (value, node)
            self.n += 1

        if self.n > len(self.table):
            self.rehash(2 * len(self.table))

    def __delitem__(self, key):
        i = self.h(key)
        _, node = self.table[i][key]
        self.order.delete_node(node)              # O(1) removal from DLL
        del self.table[i][key]
        self.n -= 1

        if self.n < len(self.table) // 4:
            self.rehash(len(self.table) // 2)

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        for key in self.order:                    # DLL __iter__ yields in FIFO order
            yield key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]  # captured in FIFO order
        self.__init__(new_size)                   # resets self.order
        for key, val in old:
            self[key] = val                       # re-inserts in FIFO order
