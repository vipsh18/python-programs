class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Lis is empty!")
            return
        trav = self.head
        while trav:
            print(trav.data, " ")
            trav = trav.next

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        trav = self.head
        while trav:
            trav = trav.next
        trav.next = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        trav = self.head
        while i < index - 1 and trav:
            trav = trav.next
            i += 1
        if not trav: print("Index Out Of Bounds!")
        else: 
            new_node = Node(data)
            new_node.next = trav.next
            trav.next = new_node


ll = LinkedList()
ll.insert_at_tail(5)
ll.insert_at_tail(10)
ll.insert_at_tail(15)
ll.traverse()