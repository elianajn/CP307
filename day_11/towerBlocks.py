from datastructures.HashTable import HashTable
import math

def towerBlocks(block_sizes, desired_height):
    i = len(block_sizes) - 1
    dictionary = HashTable()
    current_height = 0
    while current_height < desired_height and i >= 0:
        diff = desired_height - current_height
        if block_sizes[i] > diff:
            dictionary.put(block_sizes[i], 0)
            i -= 1
            continue
        n = math.floor(diff / block_sizes[i])
        current_height += (n * block_sizes[i])
        dictionary.put(block_sizes[i], n)
        i -= 1
    if current_height == desired_height:
            # i -= 1
        while i >= 0:
            dictionary.put(block_sizes[i], 0)
            i -= 1
    return dictionary


def toString(block_sizes, dictionary):
    print("{", end='')
    for i in range(dictionary.size()):
        if i != 0:
            print(", ", end='')
        key = block_sizes[i]
        value = int(dictionary.get(key))
        if value == None:
            continue
        print("%d: %d" % (key, value), end='')
    print("}")


def main():
    blocks = [1, 5, 7]
    dict = towerBlocks(blocks, 4)
    toString(blocks, dict)

    blocks = [1, 5, 7]
    dict = towerBlocks(blocks, 6)
    toString(blocks, dict)

    blocks = [2, 5, 9]
    dict = towerBlocks(blocks, 6)
    toString(blocks, dict)

    blocks = [1, 5, 7]
    dict = towerBlocks(blocks, 13)
    toString(blocks, dict)

    blocks = [2, 5, 7]
    dict = towerBlocks(blocks, 13)
    toString(blocks, dict)

main()
