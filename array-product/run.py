'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
'''

def find_product(arr):
    products = []
    for i in range(len(arr)):
        prod = 1
        cur_iter = (i + 1) % len(arr)
        while cur_iter != i:
            prod *= arr[cur_iter]
            cur_iter = (cur_iter + 1) % len(arr)
        products.append(prod)
    return products
orig = [1,2,3,4,5]
sum = find_product(orig)
print(sum)
