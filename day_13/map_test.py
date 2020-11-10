from datastructures.Graph import Graph


g = Graph()
# big = 0
# with open("roads_CA.txt") as file:
#     for line in file:
#         if line[0] == '#':
#             continue
#         n1, n2 = (int(s) for s in line.split())
#         if n1 > big:
#             big = n1
#         if n2 > big:
#             big = n2
#         if n1 > big:
#             big = n1

# print(big)
g.loadGraphDataset("roads_CA.txt")
path = g.findShortestPath(0, 3)
print("path 0 to 3: ", path)
path = g.findShortestPath(0, 50)
print("path 0 to 50: ", path)
path = g.findShortestPath(180, 19075)
print(path)
