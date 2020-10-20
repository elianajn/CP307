import random
import time
import matplotlib.pyplot as plt

def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

def generateRandomIntegers(n):
    list = []
    for i in range(n):
        list.append(random.randint(0,n))
    return list


def main():
    # list = generateRandomIntegers(100)
    # print(list)
    # insertionSort(list)
    # print(list)
    list_length = []
    list_time = []
    for i in range(500):
        ls = generateRandomIntegers(i)
        start = time.perf_counter()
        insertionSort(ls)
        end = time.perf_counter()
        elapsed = end - start
        list_length.append(i)
        list_time.append(elapsed)
    plt.xlabel("Input list size")
    plt.ylabel("Running time")
    plt.plot(list_length, list_time)
    plt.show()

main()
