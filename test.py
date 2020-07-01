class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def traverse(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head 
        while (temp):
            print(temp.data) 
            temp = temp.next
        

if __name__ == "__main__":
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(37)
    node1.next = node2
    node2.next = node3
    node2.traverse()
