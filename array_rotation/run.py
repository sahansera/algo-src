# Implement your function below.
def is_rotation(list1, list2):
    # since len is same we can use single iteration
    if len(list1) != len(list2):
        return False

    start_val = list1[0]
    start_index = -1

    for i, n in enumerate(list2):
        if n == start_val:
            start_index = i

    if start_index == -1:
        return False

    p1 = 0
    p2 = start_index
    found_sol = False

    while p1 < len(list1):
        if p2 > len(list2) - 1:
            p2 = 0
        if list1[p1] != list2[p2]:
            return False
        elif list1[p1] == list2[p2]:
            p2 += 1
            p1 += 1
    return True

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# print is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# print is_rotation(list1, list2b) #should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
print is_rotation(list1, list2c) #should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
