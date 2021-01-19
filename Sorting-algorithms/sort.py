import random
import datetime

def printMethodList():
    print('1: Insertion Sort')
    print('2: Selection Sort')
    print('3: Merge sort')
    print('4: Heap sort')
    print('5: Quick sort')
    print('6: Bubble sort')
    print('7: Shell sort')
    #print('8: ... sort')

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        # Move elements of arr[0..i-1], that are greater than key, to one position 
        # ahead of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
def selectionSort(arr):
    for i in range(len(arr)): 
        # Find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
        # Swap the found minimum element with the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def partition(arr, low, high): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] <= pivot: 
  
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n/2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap /= 2

while(True):
## Step 1: Get list of numbers to sort
    
    # Option 1: Generate list with random ints of size USER_INPUT
    array = []
    print()

    while(True):
        try: size = int(input('How many numbers would you like to sort?: '))
        except: size = 0
        if(not size in range(1, 10000)): print('\nEnter a number between 1 and 10,000')
        else: break

    for i in range(size):
        array.append( random.randint(0, 9999) )

    unsorted = array

    # Option 2: Have user input ints of size USER_INPUT
    # Option 3: Generate list with random ints based on a seed of size USER_INPUT

## Step 2: Choose sorting method
    while(True):
        method = 0
        array = unsorted
        print(unsorted)

        print('\nMethod List: ')
        printMethodList()

        while(not method in range(1, 8)):
            try: method = int(input('What method would you like to use?: '))
            except: method = 0
            if (not method in range(1, 8)):
                print('\nEnter a number between 1 and 7.')
    
        tStart = datetime.datetime.now()
        if(method == 1): insertionSort(array)
        elif(method == 2): selectionSort(array)
        elif(method == 3): mergeSort(array)
        elif(method == 4): heapSort(array)
        elif(method == 5): quickSort(array, 0, len(array)-1 )
        elif(method == 6): bubbleSort(array)
        elif(method == 7): shellSort(array)

        tEnd = datetime.datetime.now()
        tTotal = tEnd - tStart
## Step 3: Sort
    # Idea 1: Print out sorted array with time tTotal = tEnd - tStart
        print('\n', array)
        print('Time: ', tTotal)

## Break loops:
        print()
        answer = ''
        while(True):
            try: answer = input("Would you like to try another method? (Y/N): ")
            except: answer = ''
            if (answer.lower() == 'y' or answer.lower() == 'n'): break
            else: print("\nEnter 'Y' for yes or 'N' for no.")
        if( answer.lower() == 'n' ): break

    print()
    answer = ''
    while(True):
        try: answer = input("Okay. Would you like to try another list? (Y/N): ")
        except: answer = ''
        if (answer.lower() == 'y' or answer.lower() == 'n'): break
        else: print("\nEnter 'Y' for yes or 'N' for no.")
    if( answer.lower() == 'n' ): break

print('\nThank you!')