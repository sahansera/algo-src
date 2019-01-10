'''
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''

def find_subset(arr):
	sorted_arr = sorted(arr)
	sorted_set = sorted(set(sorted_arr), reverse=True)
	print(len(sorted_set))

find_subset([5,1,3,5,2,3,4,1])		
