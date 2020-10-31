import random
from datastructures.AVLTree import AVLTree

def main():
    t = AVLTree()
    for i in range(20):
        r = random.randint(1, 100)
        t.insert(r)
    # print(t.root)
    t.saveImage("avltree.jpg")

main()
