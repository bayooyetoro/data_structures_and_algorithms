# Queue implementation through LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def enqueue(self, value):
        new_item = Node(value)
        if not self._size:
            self.head = self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
            self._size += 1
        return self
    
    def dequeue(self):
        if not self._size:
            raise Exception("Empty Queue")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._size -= 1
        return former_head.value
    
    def clear_queue(self):
        self.head = None
        self.tail = None
        self._size = 0
    