class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.value})"
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def appendNode(self, data):
        newNode = Node(data)

        if not self._length:
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail 
            self.tail.next = newNode
            self.tail = newNode
        self._length += 1
        return self
    
    
dll = DoubleLinkedList()

dll.appendNode(3).appendNode(10).appendNode(15).appendNode(50)

print("Head:",dll.head.value)
print("Tail:", dll.tail.value)
print("Tail Prev:", dll.tail.prev)
print("Head Next:", dll.head.next)

