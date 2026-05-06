from ctypes import py_object  # provides low-level arrays
from random import randrange

from UnsortedArrayMap import UnsortedArrayMap


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

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]

        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.h(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)

        if new_size > old_size:
            self.n += 1

        if self.n > len(self.table):
            self.rehash(2 * len(self.table))

    def __delitem__(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]

        del curr_bucket[key]
        self.n -= 1

        if self.n < len(self.table) // 4:
            self.rehash(len(self.table) // 2)

    def __contains__(self, key):
        try:
            val = self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)

        for key, val in old:
            self[key] = val
