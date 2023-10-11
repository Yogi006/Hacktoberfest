class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        index = hash(key) % self.size
        self.table[index] = value

    def get(self, key):
        index = hash(key) % self.size
        return self.table[index]
