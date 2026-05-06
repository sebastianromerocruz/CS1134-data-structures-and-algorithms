from ctypes import py_object  # provides low-level arrays


def make_array(n):
    return (n * py_object)()


class StaticArrayQueue:
    def __init__(self, max_cap):
        self.data_arr = make_array(max_cap)
        self.capacity = max_cap
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return self.n == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        elif self.is_empty():
            self.data_arr[0] = item
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = item
            self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1

        if self.is_empty():
            self.front_ind = None

        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.data_arr[self.front_ind]


class ArrayQueue:
    INITIAL_CAPACITY = 8  # static constant

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None

    def is_empty(self):
        return len(self) == 0

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind

        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity

        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0

    def enqueue(self, elem):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        if self.is_empty():
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1

        if self.is_empty():
            self.front_ind = None

        if self.n < self.capacity // 4 and self.capacity > ArrayQueue.INITIAL_CAPACITY:
            self.resize(self.capacity // 2)

        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.data_arr[self.front_ind]

    def __len__(self):
        return self.n


if __name__ == "__main__":
    q = ArrayQueue()

    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(8)

    print(q.dequeue())  # 2
    print(q.dequeue())  # 4
    print(q.dequeue())  # 6

    q.enqueue(10)
    q.enqueue(12)
