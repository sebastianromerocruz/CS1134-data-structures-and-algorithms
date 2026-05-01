class ArrayMinHeap:
    class Item:
        def __init__(self, priority, value=None):
            self.priority = priority
            self.value = value

        def __le__(self, other):
            return self.priority <= other.priority


    def __init__(self, priorities_lst=None, values_lst=None):
        self.data = [None]
        # add later
        
        if priorities_lst is not None:
            for i in range(len(priorities_lst)):
                new_item = ArrayMinHeap.Item(priorities_lst[i], values_lst[i])
                self.data.append(new_item)
                
            first_non_leaf_ind = self.parent(len(self.data) - 1)
            
            for i in range(first_non_leaf_ind, 0, -1):
                self.fix_down(i)

    def left(self, j):
        return 2 * j

    def right(self, j):
        return 2 * j + 1

    def parent(self, j):
        return j // 2

    def has_left(self, j):
        return self.left(j) <= len(self.data) - 1

    def has_right(self, j):
        return self.right(j) <= len(self.data) - 1

    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return len(self) == 0

    def min(self):
        if (self.is_empty()):
            raise Exception("Priority queue is empty.")
        item = self.data[1]
        return item

    def insert(self, priority, value=None):
        new_item = ArrayMinHeap.Item(priority, value)
        self.data.append(new_item)
        
        self.fix_up(len(self.data) - 1)

    def delete_min(self):
        if (self.is_empty()):
            raise Exception("Priority queue is empty.")
        self.swap(1, len(self.data) - 1)
        item = self.data.pop()
        if (not self.is_empty()):
            self.fix_down(1)
        return item

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def fix_up(self, j):
        curr_ind = j
        keep_going = True
        while ((keep_going == True) and (curr_ind > 1)):
            parent_ind = self.parent(curr_ind)
            if (self.data[parent_ind] <= self.data[curr_ind]):
                keep_going = False
            else:
                self.swap(curr_ind, parent_ind)
                curr_ind = parent_ind

    def fix_down(self, j):
        curr_ind = j
        keep_going = True
        
        while keep_going == True and self.has_left(curr_ind) == True:
            if self.has_right(curr_ind) == True:
                left_ind = self.left(curr_ind)
                right_ind = self.right(curr_ind)
                
                if self.data[right_ind] <= self.data[left_ind]:
                    small_child_ind = right_ind
                else:
                    small_child_ind = left_ind
            else:
                small_child_ind = self.left(curr_ind)

            if self.data[curr_ind] <= self.data[small_child_ind]:
                keep_going = False
            else:
                self.swap(curr_ind, small_child_ind)
                curr_ind = small_child_ind