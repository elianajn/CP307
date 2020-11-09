from datastructures.HashTable import HashTable
from datastructures.Queue import Queue
from os import path
import pickle
import time

class Node:

    def __init__(self, id):
        self.node = id
        self.neighbors = []

    def addNeighbor(self, new_neighbor):
        self.neighbors.append(new_neighbor)


class Graph:

    def __init__(self):
        self.nodes = HashTable()

    def loadGraphDataset(self, filename):
        if path.exists("save.p"):
            print("Getting serialized Graph")
            self.nodes = pickle.load( open( "save.p", "rb" ) )
        else:
            with open(filename) as file:
                for line in file:
                    if line[0] == '#':
                        continue
                    n1, n2 = (int(s) for s in line.split()) # https://stackoverflow.com/questions/7395047/what-are-python-implementation-of-nextint-hasnext-from-java
                    if not self.nodes.hasKey(n1):
                        self.nodes.put(n1, Node(n1))
                    if not self.nodes.hasKey(n2):
                        self.nodes.put(n2, Node(n2))
                    self.nodes.get(n1).addNeighbor(n2)
                    # self.nodes.get(n2).addNeighbor(n1) # file has repitition so not necessary
            print("Serializing Graph")
            pickle.dump( self.nodes, open( "save.p", "wb" ) )
            file.close

    def findShortestPath(self, start, end):
        visited = [False] * self.nodes.size()
        queue = Queue()
        queue.enqueue((start,[]))
        while queue.size() > 0:
            (node_id, path) = queue.dequeue()
            visited[node_id] = True
            path.append(node_id)
            if node_id == end:
                return path
            node = self.nodes.get(node_id)
            for neighbor in node.neighbors:
                if not visited[neighbor]:
                    queue.enqueue((neighbor, path))
            # time.sleep(0.01)
        return []
