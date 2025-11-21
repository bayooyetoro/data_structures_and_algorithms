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
    

    def prepend(self, data):
        newNode = Node(data)

        if not self._length:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self._length += 1
        return self
    
    def pop_left(self):

        if not self._length:
            raise Exception("Empty List")
        
        head_to_pop = self.head
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = head_to_pop.next
            self.head.prev = None
            head_to_pop.next = None
        self._length -= 1
        return head_to_pop.value 
    

    def pop_right(self):
        if not self._length:
            raise Exception("Empty List")
        
        tail_to_pop = self.tail
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = tail_to_pop.prev
            self.tail.next = None
            tail_to_pop.prev = None
        self._length -= 1
        return tail_to_pop.value 
    
    def remove_node(self, data):
        if not self._length:
            raise Exception("Empty List")
        if self.head.value == data:
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next

        while current_node is not None and current_node.value != data:
            previous_node = current_node
            current_node = current_node.next 

        if current_node is None:
            raise Exception("Value not found in the list")
            
        if current_node.next == None:
            return self.pop_right()

        current_node.next.prev = current_node.prev
        current_node.prev.next = current_node.next

        current_node.next = None
        current_node.prev = None
        self._length -= 1
        return current_node.value

dll = DoubleLinkedList()

dll.appendNode(3).appendNode(50).appendNode(100).remove_node(150)

print("Head:",dll.head.value)
print("Tail:", dll.tail.value)
print("Tail Prev:", dll.tail.prev)
print("Head Next:", dll.head.next)

