from . LinkedList import LinkedList

class HashTable:
    def __init__(self, size=1971281):
        self.current_size = 0
        self.data = [None] * size # we want this to be statically sized
        self.array_size = size

    def size(self):
        return self.current_size

    def hashFunction(self, key):
        # assume key is an integer
        return key % self.array_size

    def put(self, key, value):
        index = self.hashFunction(key) # where it should be mapped to
        if self.data[index] == None:
            self.data[index] = LinkedList()
        self.data[index].add((key,value))
        self.current_size += 1

    def get(self, target_key):
        index = self.hashFunction(target_key)
        ll = self.data[index]
        # print(ll.size())
        list_index = 0
        # print("key: ", target_key)
        while list_index < ll.size() and ll[list_index][0] != target_key: #gets the index node
            list_index += 1
        # print("list index: ", list_index)
        # print("list size: ", ll.size())
        # print(self.hasKey(target_key))
        value = ll[list_index][1] # what if it's not there?
        return value

    def delete(self, target_key):
        index = self.hashFunction(target_key)
        ll = self.data[index]
        if ll == None:
            return
        list_index = 0
        while list_index < ll.size():
            if ll[list_index][0] == target_key:
                ll.delete(list_index)
                if ll.size() == 0:
                    self.data[index] = None
                return
            list_index += 1
        self.current_size -= 1
        # ll.delete(list_index)

    def hasKey(self, target_key):
        index = self.hashFunction(target_key)
        ll = self.data[index]
        if ll == None:
            return False
        list_index = 0
        while list_index < ll.size() and ll[list_index][0] != target_key:
            list_index += 1
        if list_index == ll.size()-1 and ll[list_index][0] != target_key:
            return False
        return True


def main():
    ht = HashTable()
    ht.put(23, "ella")
    ht.put(70, "mars")
    ht.put(6, "nocturnal")
    ht.put(1, "moo")
    ht.put(21, "medee")
    ht.put(41, "golden")
    print(ht.get(23))
    print(ht.get(6))
    print(ht.get(1))
    print(ht.get(21))
    print(ht.hasKey(6))
    ht.delete(6)
    print(ht.hasKey(6))


if __name__ == "__main__":
    main()
