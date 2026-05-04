class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()   # sentinel LRU end
        self.tail = Node()   # sentinel MRU end
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.val


    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value          # update in place
            self._remove(node)        # detach from current position
            self._add_to_tail(node)   # move to MRU end
        else:
            node = Node(key, value)
            self.map[key] = node
            self._add_to_tail(node)
            if len(self.map) > self.cap:
                lru = self.head.next
                self._remove(lru)
                del self.map[lru.key]
