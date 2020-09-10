#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if item == 0 or item == 1:
        return 1
    else:
       return item * linear_search(item - 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, 0, len(array) - 1)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    
    left = 0
    right = len(array) -1

    # while left <= right:
    middle_index = len(left + right) // 2
    
    #base case
    if item == array[middle_index]:
        return middle_index
    #move pointer
    elif item < array[middle_index]:
        right = middle_index -1
    #move pointer
    elif item > array[middle_index]:
        left = middle_index + 1




def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    # if left is None and right is None:
    

    middle_index = (right - left) // 2
    #base case
    if item == array[middle_index]:
        return middle_index
    #2nd base case
    if left >= right:
        return None
    #recursive cases
    elif item < array[middle_index]: # item is on the right side
        right = middle_index - 1
        binary_search_recursive(array, item, left, right)

    elif item < array[middle_index]: # item is on the left side
        left = middle_index + 1
        binary_search_recursive(array, item, left, right)

