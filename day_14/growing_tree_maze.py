'''
Automatically generate a maze using the growing tree algorithm.
Run from the command line in the following way:

    python growing_tree_maze.py <maze_size> <filetype>

The output will be called something like maze.txt or maze.jpg.

Examples:
    # Generate a JPG image of a 51x51 maze
    python growing_tree_maze.py 51 jpg

    # Generate a textfile maze of size 23x23
    python growing_tree_maze.py 23 txt
'''

__author__ = "Matthew"
__version__ = 0.0000001

import random
import sys
from PIL import Image

WALL = '*'
SPACE = ' '

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 180, 180)

class Maze:

    def __init__(self, size):
        self.size = size
        self.cells = []
        for i in range(size):
            row = [WALL] * size
            self.cells.append(row)

    def __getitem__(self, index):
        x, y = index
        return self.cells[x][y]

    def __setitem__(self, index, value):
        x, y = index
        self.cells[x][y] = value


    def __iter__(self):
        for row in self.cells:
            for value in row:
                yield value

    def __str__(self):
        result = ""
        for row in self.cells:
            for value in row:
                result += str(value) + " "
            result += "\n"
        return result

    def toTextfile(self, output_filename, border=True):
        textfile = open(output_filename, 'w')
        if border:
            textfile.write("%s\n" % ('#'*(self.size+2)))
        for i in range(len(self.cells)):
            row = self.cells[i]
            if border:
                textfile.write("#")
            for j in range(len(row)):
                if self[(i, j)] == WALL:
                    textfile.write("#")
                else:
                    textfile.write(" ")
            if border:
                textfile.write("#")
            textfile.write("\n")

        if border:
            textfile.write("%s\n" % ('#'*(self.size+2)))
        textfile.close()


    def toImage(self, output_filename):
        bitmap_image = Image.new("RGB" , (self.size, self.size))
        for i in range(len(self.cells)):
            row = self.cells[i]
            for j in range(len(row)):
                if self[(i, j)] == WALL:
                    bitmap_image.putpixel((i, j), BLACK)
                else:
                    bitmap_image.putpixel((i, j), WHITE)
        bitmap_image.save(output_filename)


    def neighborsUnmade(self, index):
        x, y = index
        unmades = []

        low_x = max(x-2, 0)
        low_y = max(y-2, 0)
        high_x = min(x+2, self.size-1)
        high_y = min(y+2, self.size-1)

        if self[(low_x, y)] == WALL:
            unmades.append((low_x, y))
        if self[(x, high_y)] == WALL:
            unmades.append((x, high_y))
        if self[(x, low_y)] == WALL:
            unmades.append((x, low_y))
        if self[(high_x, y)] == WALL:
            unmades.append((high_x, y))

        return unmades


    def carve(self, index1, index2):
        x1, y1 = index1
        x2, y2 = index2

        avg_x = int((x1+x2)/2.)
        avg_y = int((y1+y2)/2.)

        self[(avg_x, avg_y)] = SPACE
        self[(x2, y2)] = SPACE



    def growingTree(self):
        cell_list = [(0, 0)]
        self.carve((0, 0), (0, 0))

        while len(cell_list) > 0:
            random_cell = random.choice(cell_list)
            unmades = self.neighborsUnmade(random_cell)
            if len(unmades) > 0:
                unmade = random.choice(unmades)
                self.carve(random_cell, unmade)
                cell_list.append(unmade)
            else:
                cell_list.remove(random_cell)


if __name__=="__main__":
    size = int(sys.argv[1])
    # sizes have to be odd
    if size % 2 == 0:
        size = size + 1
    filetype = sys.argv[2].lower()  # txt, jpg, png, bmp
    m = Maze(size)
    m.growingTree()
    if filetype == "txt":
        m.toTextfile("maze.txt")
    elif filetype == "jpg" or filetype == "png" or filetype == "bmp":
        m.toImage("maze.%s" % filetype)
