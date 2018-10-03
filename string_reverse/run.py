### Solution 1 - Without Python's Utility classes
def str_reverse(sentence):
    sentence = sentence.strip()
    chArr = sentence.split()
    outStr = ''
    isPrevSpace = False
    
    for i in range(len(chArr), 0, -1):
        outStr += chArr[i - 1] + ' '
    return outStr

str_reverse("  yo this    is test   ")