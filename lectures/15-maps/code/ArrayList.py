from ctypes import py_object  # provides low-level arrays


def make_array(n):
    return (n * py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]

        self.data_arr = new_array
        self.capacity = new_size

    def append(self, val):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)

        self.data_arr[self.n] = val
        self.n += 1

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def pop(self, index=None):
        if len(self) == 0:
            raise Exception("list is empty")

        if index is None:
            index = self.n - 1

        if not (0 <= index <= self.n - 1):
            raise IndexError("invalid index")

        val = self.data_arr[index]

        for i in range(index, self.n - 1):
            self.data_arr[i] = self.data_arr[i + 1]

        self.n -= 1

        if self.n < self.capacity // 4:
            self.resize(self.capacity // 2)

        return val

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if not (0 <= ind <= self.n - 1):
            raise IndexError("invalid index")

        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if not (0 <= ind <= self.n - 1):
            raise IndexError("invalid index")

        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  # could also yield self[i]
