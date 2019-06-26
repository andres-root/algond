

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
    
    def append(self, value):
        """ Append a value to the end of the list. """

        if self.head == None:
            self.head = Node(value)
        else:
            node = self.head

            while node.next is not None:
                node = node.next
            
            node.next = Node(value)
        
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """

        node = self.head
        
        while node.next is not None:
            if node.value == value:
                return node
            node = node.next
            
        return None
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        node = self.head
        prev_node = node

        while node is not None:
            if node.value == value:
                prev_node.next = node.next
                prev_node = node
                return
            
            prev_node = node
            node = node.next
                
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        
        node_value = self.head.value
        
        self.head = self.head.next
        
        return node_value
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        
        node = self.head
        prev_node = node

        if pos > self.size():
            self.append(value)
    
            return
        else:
            if pos == 0:
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node

                return
                
            i = 0
    
            while node.next is not None:
                if i == pos:
                    new_node = Node(value)
                    new_node.next = node
                    prev_node.next = new_node
                    prev_node = node
                    return
                
                prev_node = node
                node = node.next

                i += 1
    
    def size(self):
        """ Return the size or length of the linked list. """
        
        node = self.head
        size = 0
        
        while node is not None:
            size += 1
            node = node.next
        
        return size
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


## Tests
# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
