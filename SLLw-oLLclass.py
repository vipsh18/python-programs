# Singly Linked List w/o LinkedList class
# Do we really need LLs in Python? Yes, we do but you don't know about that!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next

    def countNodes(self):
        node = self
        count = 0
        while node != None:
            count += 1
            node = node.next
        print("Number of nodes:", count) 

    def removeDuplicates(self):
        els = []
        node = self
        previous = None
        while node != None:
            if node.data in els: previous.next = node.next
            else: els.append(node.data)
            previous = node
            node = node.next

    def kth_to_last(self, k):
        if k < 0: return None
        
        
if __name__ == "__main__":
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(37)
    node4 = Node(12)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.traverse()
    node1.countNodes()
    node1.removeDuplicates()
    node1.traverse()