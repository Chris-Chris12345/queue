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
    def __init__(self,size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size
    
    def enqueue(self,item):
        if self.available == 0:
            print("The queue is full!")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available = self.available - 1
    
    def dequeue(self,item):
        if self.available == 0:
            print("The queue is empty!")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available = self.available + 1

    def peak(self):
        print(self.queue[self.front])

    def getrear(self):
        print(self.queue[self.rear])

    def show(self):
        print(self.queue)

que1 = Queue(3)

que1.enqueue(10)
que1.peak()
que1.show()
que1.enqueue(20)
que1.enqueue(30)
que1.enqueue(40)
que1.getrear()
que1.show()