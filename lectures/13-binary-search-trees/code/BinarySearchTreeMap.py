class BinartSearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if self.right is not None:
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)


    # returns value, or raises exception if not found
    def __getitem__(self, key):
        node = self.find_node(key)
        if node is None:
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # return node with key, or None if not found
    def find_node(self, key):
        cursor = self.root
        
        while cursor is not None:
            if cursor.item.key == key:
                return cursor
            elif cursor.item.key > key:
                cursor = cursor.left
            else: # (cursor.item.key < key
                cursor = cursor.right
                
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.find_node(key)
        
        if node is not None:
            node.item.value = value
        else:
            self.insert(key, value)

    # assumes that key is not in the tree
    def insert(self, key, value):
        new_item = BinartSearchTreeMap.Item(key, value)
        new_node = BinartSearchTreeMap.Node(new_item)
        
        if self.is_empty() == True:
            self.root = new_node
            self.n = 1
        else:
            parent = None
            cursor = self.root
            
            while cursor is not None:
                parent = cursor
                if(key < cursor.item.key):
                    cursor = cursor.left
                else:
                    cursor = cursor.right
                    
            if key < parent.item.key:
                parent.left = new_node
            else:
                parent.right = new_node
                
            new_node.parent = parent
            self.n += 1


    # raises an exceprion if ket not in the tree
    def __delitem__(self, key):
        node = self.find_node(key)
        
        if node is None:
            raise KeyError(str(key) + " not found")
        else:
            self.delete_node(node)

    # assumes the key is in the tree + returns item that was removed from the tree
    def delete_node(self, node_to_delete):
        item = node_to_delete.item
        num_children = node_to_delete.num_children()

        if node_to_delete is self.root:
            if num_children == 0:
                self.root = None
                node_to_delete.disconnect()
                self.n -= 1

            elif num_children == 1:
                if self.root.left is not None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                    
                self.root.parent = None
                node_to_delete.disconnect()
                self.n -= 1

            else:  # num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete_node(max_of_left)
        else:
            if(num_children == 0):
                parent = node_to_delete.parent
                
                if node_to_delete is parent.left:
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.n -= 1

            elif num_children == 1:
                parent = node_to_delete.parent
                if node_to_delete.left is not None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                if node_to_delete is parent.left:
                    parent.left = child
                else:
                    parent.right = child
                child.parent = parent

                node_to_delete.disconnect()
                self.n -= 1

            else: #(num_children == 2)
                max_in_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_in_left.item
                self.delete_node(max_in_left)

        return item

    def subtree_max(self, subtree_root):
        cursor = subtree_root
        
        while cursor.right is not None:
            cursor = cursor.right
            
        return cursor

    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                return
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key
