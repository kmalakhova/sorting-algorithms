def insertion_sort(array):
    i = 1
    while i < len(array):
        to_insert = array[i]
        j = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i]
        while j > 0 and array[j-1] > to_insert:
            array[j] = array[j-1]
            j -= 1
        array[j] = to_insert
        i += 1

"""
Loop through the entire list with i representing the first position of the unsorted sub-array
Store the first element of the unsorted list in a temporary variable called to_insert
Find the correct index to insert the value to_insert
Loop through the sorted list from back to front
Compare the values between the item at the position we're inspecting, and to_insert
Swap if needed
Increase the outer index i so that the sorted list grows, and the unsorted list shrinks
"""
