def find_max_subarray(arr):
	total_max = 0
	cur_max = 0

	for i in range(0, len(arr)):
		if arr[i] + cur_max > cur_max:
			cur_max = cur_max + arr[i]
		else:
			cur_max = 0
		total_max = max(cur_max, total_max)
	return total_max
x = [-5,1,2,3,-8]
sum = find_max_subarray(x)
print(sum)	
