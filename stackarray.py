class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0
    
    def push(self, obj):
        self._data.append(obj)

    def pop(self):
        if self.isEmpty():
            raise Empty("Stack Is Empty!")
        return self._data.pop()

    def top(self):
        if self.isEmpty():
            raise Empty("Stack Is Empty!")
        return self._data[-1]


if __name__ == "__main__":
    s = ArrayStack()
    s.push(10)
    s.push(20)
    print('Stack:', s._data)
    print('Length:', len(s))
    print('isEmpty:', s.isEmpty())
    print('Popped:', s.pop())
    print('Stack:', s._data)
    print('Popped:', s.pop())
    print('isEmpty:', s.isEmpty())
    print('Stack:', s._data)
    s.push(30)
    s.push(40)
    print('Top Element:', s.top())
    print('Stack:', s._data)