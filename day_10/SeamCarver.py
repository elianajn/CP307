import random
import sys
from PIL import Image
import numpy as np
from matplotlib import image
import scipy.signal
from scipy.signal import convolve2d

# got most of this from Matthew's video
class SeamCarver:

    def __init__(self, filename):
        self.full_im = Image.open(filename)
        self.im = image.imread(filename)[:, :, 2]
        self.rows, self.cols = self.im.shape

    def gradients(self):
        hkernel = np.array([[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]])

        vkernel = np.array([[-1, -2, -1],
                            [0, 0, 0],
                            [1, 2, 1]])
        hgrads = convolve2d(self.im, hkernel, mode="same", boundary="symm")
        vgrads = convolve2d(self.im, vkernel, mode="same", boundary="symm")

        self.im_grads = np.sqrt(pow(hgrads, 2.0) + pow(vgrads, 2.0))

    def generateDisruptionMatrix(self):
        self.disruptions = np.zeros((self.rows, self.cols))
        self.disruptions[0,:] = self.im_grads[0,:]

        for row in range(1, self.rows):
            for col in range(self.cols):
                parents_start, parents_end = max(0, col-1), min(self.cols-1, col+2)
                self.disruptions[row, col] = np.min(self.disruptions[row-1, parents_start:parents_end]) + self.im_grads[row, col]

    # got this from Will Pasley
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
            seam.insert(0,curr_col)
        return seam

    def highlightSeam(self, seam):
        row = 0
        for col in seam:
            self.full_im.putpixel((col, row), (255,0, 0))
            row += 1
        self.full_im.save("new_image.png")


if __name__ == "__main__":
    # relative_filename = "city_street.png"
    # @grader: please fill in your own path to dir below
    sc = SeamCarver(sys.argv[1])
    sc.gradients()
    sc.generateDisruptionMatrix()
    seam = sc.getSeamPath()
    sc.highlightSeam(seam)
