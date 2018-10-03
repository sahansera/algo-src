def compress(input):
    dict = {}
    if input == '':
        return input
    for ch in input:
        if ch not in dict:
            dict[ch] = 1
        else:
            dict[ch] += 1

    output = ''
    for ch in dict:
        output += ch + str(dict[ch])
    return output

compress('AABBCC')