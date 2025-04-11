from Queue import Queue
from Stack import Stack
from LinkedList import Node

class Stack(Stack):
    def __init__(self):
        super().__init__()

# Check whether the paranthesis are properly balanced or not
    def __isBalanced__(self, string):
        if string is None:
            raise IndexError("No string avaliable.")
        control = {")": "(", "]": "[", "}": "{"}
        for i in string:
            if i in "([{":
                self.push(i)
            else:
                if self.isEmpty():
                    return False
                if self.pop() != control[i]:
                    return False
        return True


class Queue(Queue):
    def __init__(self):
        super().__init__()
        self.__maxHead = None
    
    def enqueue(self, element):
        self.__elements.add(element)
        
        if self.__maxHead is None:
            self.__maxHead = Node(element)
        if self.__maxHead.element < element:
            self.__maxHead = Node(element)
    
    # Find the maximum element    
    def findMax(self):
        if self.isEmpty():
            raise IndexError("Queue is empty.")
        return self.__maxHead.element
    
    
    # Rotate the queue k positions to the right by removing the first element and adding it to last
    def rotate(self, k):
        if self.isEmpty():
            raise IndexError("Queue is empty.")
        for i in range(k+1):
            self.enqueue(self.dequeue())
        return self
        
string = "[()]{[()(]()}"