# My Lab Question

''' Write a Program to do a Stack Operation where the elements of
the empty list are to be set None and set a maxlimit 
to it and raise Excpetion when the list is empty or full'''


'''This program is actually similar to CircularQueue...But instead of Queue we are iplementing Stack :)'''

class Full(Exception):
    pass

class Empty(Exception):
    pass

class ArrayStack():
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = [None]*capacity
        self.rear = 0
        self.front = capacity - 1
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size > self.capacity
    
    def display(self):
        print(self.data)
        
    def push(self,ele):
        self.data[self.rear] = ele
        self.rear += 1
        self.size += 1
        if self.is_full():
            raise Exception("Stack OverFlow")
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        self.data[self.front] = None
        self.front -= 1
        self.size -= 1
        
s = ArrayStack(10)
s.display()
print(".....................")
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.display()
print(".....................")
s.pop()
s.pop()
s.pop()
s.display()
print(".....................")
