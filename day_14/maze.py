import sys
import numpy as np
from PIL import Image

sys.setrecursionlimit(3000)
print("Recursion limit: ", sys.getrecursionlimit())

# Start at upper-leftmost position in the maze
#     Call recursive backtracker function with that location
#
#     function recursiveBacktracker(curr_location):
#       Is the curr_location the end?  If so, we're done!
#       Otherwise:
#         Get all the curr_location neighbors (not walls, of course!)
#         Go through the neighbors:
#           If we haven't already explored that neighbor location,
#             Recursively call recursiveBacktracker with neighbor as current location
#             If that recusive call found a solution, return it
#             If not, then keep checking all the neighbors
#         If we get all the way through the neighbors and no one has a solution,
#           Give up on this recursive branch and backtrack to an ancestor recursive call
#
#       path is a list of tuples

class Maze():

    def __init__(self, filename):
        maze = []
        c = 0
        with open(filename) as file:
            for line in file:
                maze.append([])
                for char in line:
                    if char == ' ':
                        maze[c].append(0)
                    else:
                        maze[c].append(1)
                c += 1
        self.maze = np.array(maze)
        self.height, self.width = self.maze.shape


    def findPath(self, start, end):
        path = self.recursiveBacktracker((start), (end), [])
        return path


    def recursiveBacktracker(self, current_location, end, path):
        if current_location == end:
            return path
        # path.append((current_location))
        row, col = current_location
        self.maze[row, col] = 2
        neighbors = self.getNeighbors(current_location)
        for neighbor in neighbors:
            nRow, nCol = neighbor
            if self.maze[nRow][nCol] != 2:
                finalPath = self.recursiveBacktracker((neighbor), (end), path[:] + [current_location])
                if finalPath != []:
                    finalPath.append(end)
                    return finalPath
        return []


    # return a list of tuples of the neighbors
    # location is a tuple
    def getNeighbors(self, location):
        row, col = location
        neighbors = []
        # RIGHT
        if self.maze[row][col+1] == 0:
            neighbors.append((row, col+1))
        # DOWN
        if self.maze[row+1][col] == 0:
            neighbors.append((row+1, col))
        # LEFT
        if self.maze[row][col-1] == 0:
            neighbors.append((row, col-1))
        # UP
        if self.maze[row-1][col] == 0:
            neighbors.append((row-1, col))
        return neighbors


    def saveImage(self, output_filename, end, path=[]):
        bitmap_image = Image.new("RGB", self.maze.shape)
        for row in range(self.maze.shape[0]):
            for col in range(self.maze.shape[1]):
                if (row, col) in path:
                    bitmap_image.putpixel((row, col), (255,0,0))
                elif self.maze[row, col] == 1:
                    bitmap_image.putpixel((row, col), (0,0,0)) # BLACK
                else:
                    bitmap_image.putpixel((row, col), (255,255,255)) # WHTIE
        # bitmap_image.putpixel(end, (0,255,0))
        bitmap_image.save(output_filename, "PNG")



if __name__ == "__main__":
    mb = Maze(sys.argv[1])
    start = (1, 1)
    end = (mb.height-2, mb.width-3)
    path = mb.findPath(start, end)
    mb.saveImage("path.png", end, path)
