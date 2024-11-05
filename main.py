class Quwu():
    def __init__(self):
        self.items=[]
        print('retrieving quwuwu')
    def enqueue(self,num):
        self.items.insert(0,num)
    def dequeue(self):
        print(self.items.pop())

Q=Quwu()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
#should print 1,2,3,4,5