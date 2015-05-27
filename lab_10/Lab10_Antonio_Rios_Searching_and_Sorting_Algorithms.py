# Antonio Rios
# April 17, 2015
# CS 136 Lab
# LAB 10: Searching and Sorting Algorithms
#
# This lab provides an opportunity to get an
# understanding of how to perform some basic
# profiling, i.e. you will measure the execution
# time of some searching and sorting algorithms
# that we covered in class.
# -------------------------------------------------------------

import random
import time


def linear_search(data, item):

    counter = 0

    for elem in data:

        counter += 1

        if elem == item:
            return True, counter-1, counter

    # This line only executes after the for loop is finished
    return False, None, counter

def binary_search(lst, to_find):

    count = 0
    low = 0
    high = len(lst) - 1

    while low <= high:

        count += 1
        mid = (low + high) // 2

        found = lst[mid]

        if found == to_find:
            return True, mid, count

        if found < to_find:
            low = mid + 1

        else:
            high = mid - 1

    return False, None, count


#--- Problem 1- Comparing execution times of Insertion vesus Selection Sort ------#
def selection_sort(in_list):

    #swap as an inner function
    def swap(in_list, index_a, index_b):

        tmp = in_list[index_a]

        in_list[index_a] = in_list[index_b]
        in_list[index_b] = tmp

    for lower_index in range(len(in_list) - 1):
        min_index = lower_index

        for compare_index in range(lower_index+1, len(in_list)):
            if in_list[min_index] > in_list[compare_index]:
                min_index = compare_index

        swap(in_list, min_index, lower_index)

def insertion_sort(in_list):

    for index in range(1, len(in_list)):

        current_value = in_list[index] # save the value, as it may be overwritten
        sorted_index = index - 1

        # keep swapping the current value until you run into something lower
        while sorted_index >= 0 and in_list[sorted_index] > current_value:
            in_list[sorted_index+1] = in_list[sorted_index]
            sorted_index -= 1

        in_list[sorted_index+1] = current_value


def main():
    # Problem 1
    start = time.clock()
    insertion_sort(list(range(10000, 0, -1)))
    end = time.clock()
    print("It took", end-start, "seconds to insertion sort the list.")

    start = time.clock()
    selection_sort(list(range(10000, 0, -1)))
    end = time.clock()
    print("It took", end-start, "seconds to selection sort the list.")

    # Problem 2
    # Variable used to store times for binary search
    binary_avg = 0
    for i in range(100):
        start = time.clock()
        binary_search(list(range(1, 100001)), random.randint(1, 100000))
        end = time.clock()
        # Adds to total time variable
        binary_avg += end-start

    # Compute average
    binary_avg /= 100
    print("The average time for binary search was", binary_avg)

    # Variable used to store times for linear search
    linear_avg = 0
    for i in range(100):
        start = time.clock()
        linear_search(list(range(1, 100001)), random.randint(1, 100000))
        end = time.clock()
        # Adds to total time variable
        linear_avg += end-start

    # Compute average
    linear_avg /= 100
    print("The average time for linear search was", linear_avg)

    print("Binary search outperformed linear search by a ratio of", linear_avg/binary_avg)


if __name__ == "__main__":
    main()
