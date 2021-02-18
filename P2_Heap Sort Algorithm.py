# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
        
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)


arr = [11, 34, 9, 5, 16, 10] 
n = len(arr) 
print("Original array:\n") 
for i in range(n):       
    print("%d " % arr[i], end = '')
heapSort(arr) 
print("\n\nSorted array:\n") 
for i in range(n):       
    print("%d " % arr[i], end = '')


OUTPUT: -

Original array:

11 34 9 5 16 10 

Sorted array:

5 9 10 11 16 34 
