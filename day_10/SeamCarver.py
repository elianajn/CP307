import random
import sys
from PIL import Image
import numpy as np
from matplotlib import image
from scipy.signal import convolve2d as scipy

class SeamCarver:

    def __init__(self, filename):
        self.full_im = Image.open(filename)

        # channel 2 mens only blue
        self.im = image.imread(filename)[:, :, 2]
        self.rows, self.cols = self.im.shape

    def calculateSobelGradients(self):
        horizontal_kernel = np.array([[-1, 0, 1],
                                      [-2, 0, 2],
                                      [-1, 0, 1]])
        vertical_kernel = np.array  ([[-1, -2, -1],
                                      [ 0,  0,  0],
                                      [ 1,  2,  1]])
        # stick this little nieghborhood on the image and multiply it by the
        # blue intensities. a single value for a center pixel
        # how much of an edge do i have

        horizontal_grads = scipy(self.im, horizontal_kernel, mode="same", boundary="symm")
        vertical_grads = scipy(self.im, vertical_kernel, mode="same", boundary="symm")
        # get a value of pixel importance
        # edge pixels are more important
        self.img_grads = np.sqrt(pow(horizontal_grads, 2.0) + pow(vertical_grads, 2.0))

    def generateDisruptionMatrix(self):
        #initialize matrix of zeros
        self.disruptions = np.zeros((self.rows, self.cols))
        # set first row manually
        self.disruptions[0, :] = self.img_grads[0, :]
        for row in range(1, self.rows):
            for col in range(self.cols):
                parents_start, parents_end = max(0, col-1), min(self.cols-1, col+2)
                self.disruptions[row, col] = np.min(self.disruptions[row-1, parents_start:parents_end]) + self.img_grads[row, col]

    def getSeamPath(self):
        curr_row = self.rows-1
        print(self.disruptions[curr_row, :])
        min_col = np.min(self.disruptions[curr_row, :])
        curr_col = np.where(self.disruptions[curr_row, :] == min_col)[0][0]
        seam = [curr_col]
        for curr_row in range(self.rows-2, -1, -1):
            print("col ", curr_col)
            parents_start, parents_end = max(0, curr_col-1), min(self.cols-1, curr_col+2)
            print(parents_start)
            print(parents_end)
            min_parent = np.min(self.disruptions[curr_row-1, parents_start:parents_end])
            min_parent_index = np.where(self.disruptions[curr_row-1, parents_start:parents_end] == min_parent)[0][0]
            curr_col += min_parent_index - 1
            seam.insert(0, curr_col)
        return seam


    def highlightSeam(self, seam):
        row = 0
        for col in seam:
            self.full_im.putpixel((co, row), (255, 0 , 0))
            row += 1
        self.full_im.save("new_image.pg")



if __name__ == "__main__":
    sc = SeamCarver(sys.argv[1])
    sc.calculateSobelGradients()
    sc.generateDisruptionMatrix()
    seam = sc.getSeamPath()
    sc.highlightSeam(seam)
