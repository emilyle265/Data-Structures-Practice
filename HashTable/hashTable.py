class HashTable:
    def __init__(self):
        '''Initialize size, slot and data.'''
        self.size = 11
        self.slot = [None]*self.size
        self.data = [None]*self.size

    def get(self, key):

    def rehash(self):

    def hashFunction(self, key, size):
        '''Give a key and the size of current HashTable.'''
        return key%size

    def put(self, key, data):
        '''Add a key and value to the HashTable.'''

        # Get hashValue by giving the hashFunction a key and size (len).
        hashvalue = self.hashFunction(key, len(self.slots))

        # if the slot at the given hashvalue is none, set the key and data at that position.
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # if the slot at hashvalue is already the key, replace the data.
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data