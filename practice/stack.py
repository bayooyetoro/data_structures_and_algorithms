class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"
    
class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        new_item = Node(value)
        new_item.next = self._top
        self._top = new_item
        self._size += 1
        return self
    
    def pop(self):
        if not self._size:
            raise Exception("Empty Stack")
        to_pop = self._top
        self._top = to_pop.next
        to_pop.next = None
        self._size -= 1
        return self


# Other implementation
from collections import deque

stack = deque()

stack.append(100)
stack.pop()

print(stack)