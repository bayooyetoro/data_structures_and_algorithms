class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next = None
   
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value:int):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self

    def prepend(self, value:int) -> 'LinkedList':
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return self

    def pop_left(self) -> 'LinkedList':
        if not self._length:
            raise Exception("Empty List")
        else:
            head_to_remove = self.head
            self.head = head_to_remove.next
            head_to_remove = None
            if not self._length:
                self.tail = None
                  
            self._length -= 1
        return None
    
    def pop_right(self):
        if not self._length:
            raise Exception("Empty List")
        if self._length == 1:
            raise Exception("Single Value List")
        else:
            current_node = self.head
            popped_node = self.tail
            while current_node.next is not self.tail:
                current_node = current_node.next

            self.tail = current_node
            self.tail.next = None
        self._length -= 1
        return popped_node.value
    
    def remove(self, value_to_pop):
        if not self._length:
            raise Exception("Empty List")
        elif value_to_pop == self.head.value:
            return self.pop_left()
        
        previous_node = self.head
        current_node = previous_node.next

        while current_node is not None and current_node.value != value_to_pop:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            raise Exception("Value not Found")
        
        if current_node.next is None:
            self.tail = previous_node

        previous_node.next = current_node.next
        current_node.next = None

        self._length -= 1
        return current_node.value

my_list = LinkedList().append(5).append(10).append(50)
print(f"Tail: {my_list.tail.value}, Head: {my_list.head.value}, Length: {my_list._length}")
my_list.remove(5)
print(f"Tail: {my_list.tail.value}, Head: {my_list.head.value}, Length: {my_list._length}")