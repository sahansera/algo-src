def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    lastIndex = len(digits) - 1
    digits[lastIndex] = digits[lastIndex] + 1
    i, j = len(digits)-1, len(digits)-2

    while(j >= 0):
        if digits[i] > 9:
            digits[i] = 0
            digits[j] = digits[j] + 1
        i -= 1
        j -= 1
    if digits[0] > 9:
        return [1,0] + digits[1:]
    return digits

print(plusOne([9,9,9,9]))
