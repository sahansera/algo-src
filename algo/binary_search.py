def binarySearch(arr, item):
    if len(arr) == 0:
        return False 
    else:
        midpoint = len(arr)//2
        if arr[midpoint] == item:
            return True 
        else:
            if item < arr[midpoint]:
                return binarySearch(arr[:midpoint], item)
            else:
                return binarySearch(arr[midpoint+1:], item)

A = [1,2,3,4,5,6]

index = binarySearch(A, 5)

print(index)
