class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = -1
        self.queue = [None for i in range(size)]
    
    def IsEmpty(self):