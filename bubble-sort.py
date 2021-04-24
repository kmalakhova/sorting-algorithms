def bubble_sort(array):
    i = 0
    # Begin the outer loop
    while i < len(array) - 1:
        j = 0
        # Begin the inner loop
        while j < (len(array) - i - 1):
            # Compare two adjacent items
            if array[j] > array[j+1]:
                # Swap
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            j += 1
        i += 1

"""
Start a variable i at 0
Create an outer loop that loops while i is smaller than the length of the array - 1 since we don't need to bubble the final value
Start a variable j at 0
Create an inner loop that loops while j is smaller than len(array) - i - 1 since we want to avoid the i sorted elements at the end, and we need to leave one extra value for the pairwise comparisons
Compare the items at index j and j+1. If they're out of order:
Swap the items at array[j] and array[j+1] using a temporary variable, temp
Increment j
Repeat until j reaches its limit
Increment i
Repeat until i reaches its limit   
"""
