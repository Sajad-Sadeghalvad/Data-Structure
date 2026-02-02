class Queue:
    def __init__(self, max = 100):
        self.queue = [] * max
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear >= len(self.queue) -1:
            print('Queue is full')
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[0] = data
            return
        self.rear += 1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print('Queue is empty')
            return
        if self.front == self.rear:
            k = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.queue[self.front]
        self.front += 1
        return k
    