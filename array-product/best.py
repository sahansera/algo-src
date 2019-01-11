'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
'''

def find_product(arr):
    products = []
    left = []
    right = [1] * len(arr)
    left.append(1)
    right.insert(len(arr), 1)
    for i in range(1, len(arr)):
        left.append(arr[i-1] * left[i-1])

    for j in range(len(arr)-2, -1, -1):
        right[j] = arr[j+1] * right[j+1]
        
    for i in range(0, len(arr)):
        products.append(left[i] * right[i])

    return products
orig = [1,2,3,4,5]
sum = find_product(orig)
print(sum)
