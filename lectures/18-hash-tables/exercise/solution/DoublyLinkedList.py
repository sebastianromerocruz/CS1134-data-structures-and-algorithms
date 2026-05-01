class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.n = 0

    def is_empty(self):
        return len(self) == 0

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        
        prev_node = node
        next_node = node.next
        
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        
        self.n += 1
        
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        data = node.data
        
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.n -= 1
        node.disconnect()
        
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        return self.delete_node(self.trailer.prev)

    def remove_all(self, elem):
        cursor = self.header.next
        
        while cursor is self.trailer:
            if cursor.data == elem:
                next_node = cursor.next
                self.delete_node(cursor)
                cursor = next_node
            else:
                cursor = cursor.next

    def __len__(self):
        return self.n
    
    def __iter__(self):
        cursor = self.header.next
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return '[' + " <--> ".join([str(elem) for elem in self]) + ']'