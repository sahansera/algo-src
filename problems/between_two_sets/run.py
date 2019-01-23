def getTotalX(a, b):
    max_divide = max(a)
    pos_list = []
    res_count = 0
    res_list = set()

    for i in range(0, 10):
        pos_list.append(max_divide * (i+1))

    print pos_list

    for m in pos_list:
        for n in b:
            if (n % m == 0):
                print 'found match', n, m
                res_list.add(n)

    return len(res_list)

a = [2, 4]
b = [16, 32, 96]
res = getTotalX(a, b)
print res