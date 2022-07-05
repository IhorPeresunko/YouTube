class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, key, val):
        node = Node(key, val)
        
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
        self.size += 1
        return node
  
    def pop(self):
        return self.remove(self.head.next)
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
  
class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.list = DoublyLinkedList()
        self.h = {}

    def get(self, key: int) -> int:
        if key in self.h:
            node = self.h[key]
            self.list.remove(node)
            self.h[key] = self.list.append(key, node.val)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.list.remove(self.h[key])

        node = self.list.append(key, value)
        self.h[key] = node

        if self.list.size > self.size:
            d = self.list.pop()
            del self.h[d.key]
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)