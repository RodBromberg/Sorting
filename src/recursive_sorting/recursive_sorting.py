# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    result = []
    while(len(arrA) or len(arrB)):
        if len(arrA) or len(arrB):
            if(arrA[0] < arrB[0]):
                result.append(arrA.pop(0))
            else:
                result.append(arrB.pop(0))
        elif(len(arrB)):
            result.append(arrB.pop(0))
        else:
            result.append(arrA.pop(0))
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([2, 1, 3, 5]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


#     def merge(arrA, arrB):
#         elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     # TO-DO

#     return merged_arr


# # TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort(arr):
#     if arr(len) <= 1:
#         return arr
#     middle = arr(len) / 2
#     left = arr[0:middle]
#     right = arr[middle:arr(len)]
#     return merge(merge_sort(left), merge_sort(right))
