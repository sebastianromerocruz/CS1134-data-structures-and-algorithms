class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        
        self.left = left
        if left is not None:
            self.left.parent = self
            
        self.right = right
        if right is not None:
            self.right.parent = self
            
        self.parent = None


if __name__ == "__main__":
    node_a  = Node(3)
    node_b = Node(25)
    root  = Node(7, node_a, node_b)
    
    print(f"\t({root.data})")
    print(f"({root.left.data})\t\t({root.right.data})")

    print(f"\n- Node ({node_a.data})'s parent is ({node_a.parent.data})")
    print(f"- Node ({node_b.data})'s parent is ({node_b.parent.data})")
    print(f"- Node ({root.data})'s parent is ({root.parent.data if root.parent else None})")
