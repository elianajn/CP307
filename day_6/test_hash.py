datastructures.HashTable import HashTable

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
