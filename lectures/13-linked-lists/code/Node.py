"""
Sebastián Romero Cruz
Linked List Node
Fall 2025
CS 1113
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def disconnect(self):
        self.data = None
        self.next = None


def traverse(head_node):
    # traversing linked list
    current = head_node
    
    while current != None:
        print(f"{current.data} -> ", end='')
        current = current.next
                

if __name__ == "__main__":
    # creating linked list
    head = Node()
    head.data = 1
    print(f"Head's data: {head.data}")
    
    # adding elements to linked list
    new_node = Node(2)
    head.next = new_node
    print(f"Head's next's data: {head.next.data}")
    
    new_node = Node(3)
    head.next.next = new_node
    print(f"Head's next's next's data: {head.next.next.data}")
    
    new_node = Node(4)
    head.next.next.next = new_node
    print(f"Head's next's next's next's data: {head.next.next.next.data}")
    
    # changing the head node of linked list
    new_node = Node(0) 
    new_node.next = head
    head = new_node
    print(f"New head's data: {head.data}")
    
    traverse(head)
