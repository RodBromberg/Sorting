# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
# def binary_search(arr, target):

#     if len(arr) == 0:
#         return -1  # array empty

#     low = 0
#     high = len(arr)-1

#     # TO-DO: add missing code

#     return -1  # not found


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        middle = low + (low + high) // 2
        guess = arr[middle]
        if(guess == target):
            return middle
        else:
            if(target < guess):
                high = middle - 1
            else:
                low = middle + 1
    return - 1


# STRETCH: write a recursive implementation of Binary Search
print(binary_search([1, 2, 3, 4, 5], 3))


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
