def quickSort(arr, start, end):
    if start >= end:
        return
    key = start
    i = start+1
    j = end
    while i<=j:
        while i <= end and arr[i] <= arr[key]:
            i = i+1
        while j > start and arr[j] >= arr[key]:
            j = j-1
        if i>j:
            temp = arr[j]
            arr[j] = arr[key]
            arr[key] = temp
        else:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    quickSort(arr, start, j-1)
    quickSort(arr, j+1, end)
    
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1
        if i < len(lefthalf):
            for t in range(i,len(lefthalf)):
                arr[k] = lefthalf[t]
                k = k+1
        else:
            for t in range(j,len(righthalf)):
                arr[k] = righthalf[t]
                k = k+1

def heapify(arr, number, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < number and arr[largest] < arr[left]:
        largest = left
    if right < number and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        heapify(arr,number,largest)

def heapSort(arr, number):
    i = number-1
    while i>=0:
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        heapify(arr,i,0)
        i = i-1
        
alist = []
n = (int)(input())

for i in range(0,n):
    alist.append((int)(input()))
j = n//2-1
while j>=0:
    heapify(alist,n,j)
    j = j-1
print(alist)
heapSort(alist,n)
print(alist)