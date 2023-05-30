class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        hash_val = 0
        for char in key:
            hash_val +=  ord(char)
        return hash_val % self.size
    
    def insert(self, key, val):
        idx = self.hash_func(key)
        slot = self.table[idx]
        for item in slot:
            if item[0] == key:
                item[1] = val
                return
        slot.append([key,val])

    def get(self, key):
        idx = self.hash_func(key)
        slot = self.table[idx]
        for item in slot:
            if item[0] == key:
                return item[1]
        return None

hash_table = HashTable(10) 
hash_table.insert("Ann", 98)
hash_table.insert("John", 100)

print(hash_table.get("Ann"))  
print(hash_table.get("John")) 
print(hash_table.get("Bob"))
print(hash_table.table)