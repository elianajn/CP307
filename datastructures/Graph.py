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
                    n1s, n2s = line.split()
                    n1 = int(n1s)
                    n2 = int(n2s)
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
        starttime = time.perf_counter()
        visited = [False] * self.nodes.size()
        queue = Queue()
        queue.enqueue((start,[]))
        while queue.size() > 0:
            (node_id, path) = queue.dequeue()
            if not visited[node_id]:
                visited[node_id] = True
                if node_id == end:
                    endtime = time.perf_counter()
                    print("BFS time: ", endtime-starttime)
                    return path[:]+[node_id]
                node = self.nodes.get(node_id)
                for neighbor in node.neighbors:
                    queue.enqueue((neighbor, path[:]+[node_id]))
        return []
