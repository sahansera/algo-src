'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def max_subarray_brute(arr):
	largest_arr = cur_largest_arr = [arr[0]]
	ptr_i = ptr_j = 1
	total_max = cur_max = arr[0]
	while (ptr_i < len(arr) - 1 and ptr_j < len(arr)-1):
		print('ptr_i', ptr_i, 'ptr_j', ptr_j)
		if cur_max < cur_max + arr[ptr_j]:
			cur_largest_arr.append(arr[ptr_j])
			cur_max += arr[ptr_j]
			ptr_j += 1
			print(cur_largest_arr)
		else:
			ptr_i += 1
			ptr_j = ptr_i + 1
			if cur_max > total_max:
				total_max = cur_max
				largest_arr = cur_largest_arr
				cur_largest_arr = []
	return largest_arr
				

sum = max_subarray_brute([-2,1,-3,4,-1,2,1,-5,4])
print(sum)
