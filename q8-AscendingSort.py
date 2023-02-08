def mergesort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        #recursion
        mergesort(left_arr)
        mergesort(right_arr)
        
        #merge
        i,j,k = 0,0,0 #i to iterate left arr, j to iterate right arr, k to iterate merged arr
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            
        while i < len(left_arr): #left array clearance
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr): #right array clearance
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
def quicksort(arr,left,right):
    if left < right:
        partPos = partition(arr, left, right)
        quicksort(arr, left, partPos - 1)
        quicksort(arr, partPos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and  arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]

    if arr[i] > pivot:
        arr[i] , arr[right] = arr[right] , arr[i]

    return i
    
n = int(input('Enter no of elements: '))
L = []
for x in range(n):
    L.append(int(input(f'Enter element {x+1}: ')))

ch = int(input('Menu: 1. Merge Sort, 2. Quick Sort. Choose: '))
res = 0
print(f'\nInput List: {L}')
if ch == 1:
    mergesort(L)
    print(f'Merge Sorted list: {L}')
elif(ch == 2):
    quicksort(L,0,len(L)-1)
    print(f'Quick Sorted list: {L}')
else:
    print('Wrong Choice.')
