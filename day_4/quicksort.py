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

def swap(ls, x, y):
    ls[x], ls[y] = ls[y], ls[x]

def partition(ls, p, q):
    x = ls[q]
    i = p - 1 # confused
    for j in range(p, q):
        if ls[j] <= x:
            i += 1
            swap(ls, i, j)
    swap(ls, i+1, q)
    return i + 1

def quicksort(ls, p, q):
    if p < q:
        partition_index = partition(ls, p, q)
        quicksort(ls, p, partition_index-1)
        quicksort(ls, partition_index+1, q)

def timing_tests(n):
    list_length = []
    insertion_time = []
    quick_time = []
    for i in range(1, n):
        print("test ", i)

        ls = generateRandomIntegers(i)
        start = time.perf_counter()
        insertionSort(ls)
        end = time.perf_counter()
        elapsed = end - start
        list_length.append(i) # ONLY DO THIS ONCE
        insertion_time.append(elapsed)

        ls = generateRandomIntegers(i)
        start = time.perf_counter()
        quicksort(ls, 0, len(ls)-1)
        end = time.perf_counter()
        elapsed = end - start
        quick_time.append(elapsed)

    return list_length, insertion_time, quick_time

def main():
    # ls = generateRandomIntegers(10)
    # print(ls)
    # quicksort(ls,0,len(ls)-1)
    # print(ls)
    list_length, insertion_time, quick_time = timing_tests(100)
    plt.xlabel("Input list size")
    plt.ylabel("Running time")
    plt.plot(list_length, insertion_time, 'g')
    plt.plot(list_length, quick_time, 'b')
    plt.show()

main()

# Is quicksort always faster than insertion sort given a particular n?
# If not, when is insertion sort faster? When is quicksort faster? Why?
# Quicksort is not always faster. Insertion was faster for less than length ~20, and above that quicksort is faster. For small lists insertion sort is probably faster because the recursive calls in quicksort slow the algorithim down more than it makes back in efficiency. Once the values get large enough the efficiency of the algorithim wins out. 
