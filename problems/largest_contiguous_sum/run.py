### Solution 1 (The only solution I could think of)

def find_sum(arr):

    if (len(arr) == 0):
        return 0

    prevSum = arr[0]
    currSum = arr[0]

    for n in arr[1:]:
        prevSum = max(prevSum+n, n)
        currSum = max(prevSum, currSum)
    return currSum

# arr1 = [1,2,3,4,5,6,-10] # Sum = 21
# arr1 = [1,2,-1,3,4,10,10,-10,-1] # Sum = 29
# arr1 = [1] # Edge cases Sum = 1

# print(find_sum(arr1))

    