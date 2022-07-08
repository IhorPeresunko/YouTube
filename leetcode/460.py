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
        if self.size > 0:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
            return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lists = collections.defaultdict(DoublyLinkedList) # { frequency: LinkedList }
        self.nodes = collections.defaultdict(Node) # { key: LinkedListNode }
        self.freq = collections.defaultdict(int) # { key: frequency }
        self.minfreq = 1
    
    def __update_frequency(self, key):
        prev_node = self.nodes[key]
        prev_freq = self.freq[key]

        prev_freq_list = self.lists[prev_freq]
        prev_freq_list.remove(prev_node)

        next_freq_list = self.lists[prev_freq + 1]
        node = next_freq_list.append(prev_node.key, prev_node.val)

        self.nodes[key] = node
        self.freq[key] = prev_freq + 1

        if prev_freq_list.size == 0:
            del self.lists[prev_freq]
            if prev_freq == self.minfreq:
                self.minfreq += 1

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        
        self.__update_frequency(key)
    
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            self.nodes[key].val = value
            self.__update_frequency(key)
            return
        
        if self.size == self.capacity:
            deleted_node = self.lists[self.minfreq].pop()
            del self.nodes[deleted_node.key]
            del self.freq[deleted_node.key]
            
            if self.lists[self.minfreq].size == 0:
                del self.lists[self.minfreq]
            
            self.size -= 1

        node = self.lists[1].append(key, value)
        self.nodes[key] = node
        self.freq[key] = 1

        self.size += 1
        self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)