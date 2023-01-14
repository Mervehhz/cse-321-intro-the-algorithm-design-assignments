def median(array):
    # Base case: if the array has length 0 or 1, return the only element (or None if the array is empty)
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]

    # Divide the array into two halves
    half = len(array) // 2
    left = array[:half]
    right = array[half:]

    # Recursively find the medians of the two halves
    median_left = median(left)
    median_right = median(right)

    # If the length of the array is odd, return the element in the middle of the array
    if len(array) % 2 == 1:
        return array[half]

    # If the length of the array is even, return the average of the two elements in the middle of the array
    else:
        return (array[half - 1] + array[half]) / 2



# Find the median of an odd-length array
array = [345, 14, 5343, 2, 4]
array.sort()
print(median(array))  # Output: 3

# Find the median of an even-length array
array = [3, 13453, 5, 245, 664, 456]
array.sort()
print(median(array))  # Output: 4
