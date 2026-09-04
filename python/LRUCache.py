class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Nós sentinela: nunca guardam dados reais, só marcam as pontas
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head