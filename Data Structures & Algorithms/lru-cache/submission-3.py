class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        next, prev = self.right, self.right.prev
        next.prev = prev.next = node
        node.prev, node.next = prev, next

    def remove(self, node):
        next, prev = node.next, node.prev
        next.prev, prev.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if self.cache and len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]
