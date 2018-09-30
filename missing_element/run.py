### Solution 1 - Without DS (BF)
### Does not work for repeating numbers
def missing(arr1, arr2):
    # Assumption: len (arr1) > len(arr2)

    for n in arr1:
        if n not in arr2:
            return n

val = missing([5,5,7,7], [5,7,7])
print(val)


### Solution 2 - With DS (+/-)
def missing2(arr1, arr2):
    seen = {}
    for n in arr1:
        if n in seen:
            seen[n] += 1
        else:
            seen[n] = 1

    for n in arr2:
        seen[n] -= 1

    for n in seen:
        if seen[n] != 0:
            return n
                

val2 = missing2([5,5,7,7], [5,7,7])
print(val2)

### Solution 3 - With XOR
def missing3(arr1, arr2):
    result = 0
    for n in arr1+arr2:
        result^= n
    return result


val3 = missing3([1,2,3,4,5,6,7], [3,7,3,2,1,4,6])
val4 = missing3([5,5,7,7], [5,7,7])

print(val4)