from stackarray import Empty

class QueueArray:
    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def enqueue(self, i):
        self._data.append(i)
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Empty("Queue Is Empty!")
        value = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front += 1
        return value

    def first(self):
        if self.isEmpty():
            raise Empty("Queue Is Empty!")
        return self._data[self._front]


q = QueueArray()
q.enqueue(10)
q.enqueue(20)
print("Queue:", q._data)
print("Length:", len(q))
print("Dequeue:", q.dequeue())
print("Queue:", q._data)
q.enqueue(30)
q.enqueue(40)
print("Queue:", q._data)
print("Front:", q.first())
print("Queue:", q._data)
print("Dequeue:", q.dequeue())
print("Queue:", q._data)
