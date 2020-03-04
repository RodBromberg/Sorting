# TO-DO: Complete the selection_sort() function below
import math


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    arr_length = len(arr)

    for i in range(arr_length):
        for j in range(0, (arr_length-i-1)):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
