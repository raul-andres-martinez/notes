# Binary search definition

Binary search utilizes the **divide and conquer** approach, along with **recursion** (which could be iterative too), to find a value in a sorted list. It only operates correctly when the list is in sorted order.

## Time and space complexity

The **time complexity of binary search is O(log n)**, where n is the number of elements in the sorted list. This efficiency arises from its ability to halve the search space in each step.

The **space complexity of binary search is O(1)**, as it requires only a constant amount of extra space for storing a few variables, regardless of the size of the input list.

## Implementation

Binary search (recursive approach) requires four parameters, 'low' and 'high', to track the portion of the array being searched, the array itself and the value to find.

During each iteration of the function, the 'mid' variable is calculated as (low + high) / 2. If the value being searched is higher than 'mid', 'low' points to 'mid + 1' (indicating the upper part of the array); otherwise, 'low' remains the same, and 'high' points to 'mid - 1' (indicating the lower part of the array).

```python
def binary_search(arr, low, high, x):
    mid = (low + high) // 2

    # Check if x is mid element and return if true
    if x == arr[mid]:
        return mid

    # Check if x is bigger than mid, indicating it's 
    # going to be present on upper part of the array
    if x > arr[mid]:
        return binary_search(arr, mid + 1, high, x)

    # Check if x is smaller than mid, indicating it's 
    # going to be present on lower part of the array
    if x < arr[mid]:
        return binary_search(arr, low, mid - 1, x)

    # Element is not present in array
    return None

# Testing binary_search
arr = [ 5, 9, 14, 22, 26, 28, 29, 32, 40]  
x = 1

print(binary_search(arr, 0, len(arr)-1, x))
```

## Exercises

### 1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

log2 128 -> log = 2^7. 
In the worst case, it would take 7 comparisons to find the result.
### 1.2 Suppose you double the size of the list. What’s the maximum number of steps now?

log2 256 -> log = 2^8
In the worst case, it would only take one more comparison, making it a total of 8.