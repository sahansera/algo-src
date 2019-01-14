'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) < 1:
        return
    idx_dict = {}

    for i in range(len(nums)):
        if nums[i] in idx_dict:
            return [idx_dict[nums[i]], i]
        else:
            idx_dict[target - nums[i]] = i


arr = [2,7,11,15]
print(twoSum(arr, 9))
