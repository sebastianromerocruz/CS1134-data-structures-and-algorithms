from random import randrange
from ctypes import py_object
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

    class Item:
        def __init__(self, k, v):
            self.key = k
            self.value = v

    def __init__(self, N=64):
        self.table = make_array(N)
        for i in range(N):
            self.table[i] = None          # empty bucket = None (saves space)
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        i = self.h(key)
        bucket = self.table[i]

        if bucket is None:
            raise KeyError(key)
        elif type(bucket) == ChainingHashTableMap.Item:
            if bucket.key == key:
                return bucket.value
            raise KeyError(key)
        else:
            return bucket[key]

    def __setitem__(self, key, value):
        i = self.h(key)
        bucket = self.table[i]

        if bucket is None:
            self.table[i] = ChainingHashTableMap.Item(key, value)
            self.n += 1
        elif type(bucket) == ChainingHashTableMap.Item:
            if bucket.key == key:
                bucket.value = value
            else:
                # promote: single Item to UnsortedArrayMap
                new_bucket = UnsortedArrayMap()
                new_bucket[bucket.key] = bucket.value
                new_bucket[key] = value
                self.table[i] = new_bucket
                self.n += 1
        else:
            old_size = len(bucket)
            bucket[key] = value
            if len(bucket) > old_size:
                self.n += 1

        if self.n > len(self.table):
            self.rehash(2 * len(self.table))

    def __delitem__(self, key):
        i = self.h(key)
        bucket = self.table[i]

        if bucket is None:
            raise KeyError(key)
        elif type(bucket) == ChainingHashTableMap.Item:
            if bucket.key != key:
                raise KeyError(key)
            
            self.table[i] = None
            self.n -= 1
        else:
            del bucket[key]
            self.n -= 1
            if len(bucket) == 0:
                self.table[i] = None
            elif len(bucket) == 1:
                # demote: UnsortedArrayMap → single Item
                remaining = next(iter(bucket))
                self.table[i] = ChainingHashTableMap.Item(remaining, bucket[remaining])

        if self.n < len(self.table) // 4:
            self.rehash(len(self.table) // 2)

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        for bucket in self.table:
            if bucket is None:
                continue
            elif type(bucket) == ChainingHashTableMap.Item:
                yield bucket.key
            else:
                yield from bucket

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        
        for key, val in old:
            self[key] = val
