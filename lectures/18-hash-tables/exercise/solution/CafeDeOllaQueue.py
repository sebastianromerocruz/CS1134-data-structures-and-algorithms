from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList


class CafeDeOllaQueue:
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.hash_table = ChainingHashTableMap()

    def __len__(self):
        return len(self.dll)

    def add(self, name, cups):
        if name in self.hash_table:
            node = self.hash_table[name]
            node.data = (name, cups)
        else:
            node = self.dll.add_last((name, cups))
            self.hash_table[name] = node

    def get_cups(self, name):
        if name not in self.hash_table:
            raise Exception(f"No order found for '{name}'")

        return self.hash_table[name].data[1]

    def prioritise(self, name, prev_name):
        if name not in self.hash_table:
            raise Exception(f"No order found for '{name}'")

        if prev_name not in self.hash_table:
            raise Exception(f"No order found for '{prev_name}'")

        data = self.dll.delete_node(self.hash_table[name])
        new_node = self.dll.add_after(self.hash_table[prev_name], data)
        self.hash_table[name] = new_node

    def cancel(self, name):
        if name not in self.hash_table:
            raise Exception(f"No order found for '{name}'")

        self.dll.delete_node(self.hash_table[name])
        del self.hash_table[name]

    def serve(self, first=1):
        count = min(first, len(self.dll))
        result = []

        for _ in range(count):
            name, cups = self.dll.delete_first()
            del self.hash_table[name]
            result.append((name, cups))

        return result
