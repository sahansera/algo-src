def find_pairs(arr, sum):
    pairs = set()
    for idx, n in enumerate(arr):
        if idx == len(arr) - 1:
            return
        if arr[idx + 1] + n == sum:
            # print(arr[idx + 1], n)
            pairs.add((arr[idx + 1], n))
            print(pairs)
    # print(pairs)
    return pairs

temp = [1,5,2,4]
print(find_pairs(temp, 7))
