class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_beginning(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return removed_data

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end("prepare")
    ll.insert_at_end("roll")
    ll.insert_at_beginning("hello")
    print(ll.remove_at_beginning())  # Should return "hello"