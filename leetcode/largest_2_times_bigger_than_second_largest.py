'''
Key Takeaways:
    1. If we need to find the second highest, check the current val with the current highest and then if it's greater, assign the current highest to second highest
    e.g. = secondHighest <- highest <- n
    This sort of works likes keeping history of previous value (we only need the recent & past value, so no point in keeping a stack

    Time: O(n)
    Space: O(1)
'''

def dominantIndex(nums):
    highestIndex = 0
    highest = -1
    secondHighest = -1

    for i, n in enumerate(nums):
        if n >= highest:
            secondHighest = highest
            highestIndex = i
            highest = n
        elif n > secondHighest:
            secondHighest = n
    if secondHighest * 2 <= highest:
        return highestIndex
    return -1
x = [3,6,4,1]
val = dominantIndex(x)
print(val)
