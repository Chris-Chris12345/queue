#Queue is to store and manage the data.
#It works on FIFO principle(first in first out).

'''
que = [None,None,None,None]
frontzero = 0
rearzero = 0

#Endqueue(5)
front = 0
rear = 1
que = [10,None,None,None]

#Endqueue(20)
front = 0
rear = 2
que = [10,20,None,None]

#Dequeue
que = [None,20,None,None]
'''


class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size

    def enqueue(self, item):
        if self.available == 0:
            print("The queue is full!")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available -= 1

    def dequeue(self):
        if self.available == self.size:
            print("The queue is empty!")
        else:
            served = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1
            print("Served:", served)

    def peek(self):
        if self.available == self.size:
            print("Queue is empty")
        else:
            print("Front customer:", self.queue[self.front])

    def show(self):
        print("Full queue:", self.queue)


que = Queue(5)

que.enqueue("Riya")
que.enqueue("Aman")
que.enqueue("Kabir")
que.dequeue()
que.enqueue("Simran")
que.peek()
que.show()
