import random
from datastructures.AVLTree import AVLTree

def main():
    t = AVLTree()
    for i in range(20):
        r = random.randint(1, 100)
        t.insert(r)
    # print(t.root)
    t.insert(6)
    # t.insert(8)
    # t.insert(9)
    # t.insert(11)
    # t.insert(12)
    t.insert(4)
    t.insert(2)
    t.insert(18)

    t.saveImage("avltree.jpg")
    t.remove(6)
    t.remove(18)
    t.saveImage("avltree_afterremoval.jpg")

main()
