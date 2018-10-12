class Queue(object):
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

q = Queue()
print(q.isEmpty())
q.enqueue(1)
print(q.size())
print(q.dequeue())
print(q.size())
