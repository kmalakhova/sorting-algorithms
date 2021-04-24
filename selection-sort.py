def selection_sort(array):
    i = 0
    while i < len(array) - 1:
        min_index = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
        i += 1

"""
Start a variable i at 0
Create an outer loop that loops while i is smaller than the length of the array - 1 since we don't need to swap the final value
Start with the assumption that the minimum value is already in the right place by setting min_index to i
Start a variable j at the position one past i to look for the smallest element in the rest of the array
Create an inner loop that loops j over the remainder of the array
If the current inspected value is smaller than the current smallest value, update min_index with the current index j
Increase j
Repeat until j reaches the end of the list
If i and min_index are not the same, then
Swap the elements at index i and index min_index using a temporary variable temp
Increase i
Repeat until i reaches the end of the list
"""