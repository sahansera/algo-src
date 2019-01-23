'''
Key Takeaways:
    1. x % 10 = gets one's place (123 => 3)
    2. x / 10 = gets the rest (123 => 12)
'''
def reverse(x):
    INT_MIN = int(-2147483648)
    INT_MAX = int(2147483647)

    remaining = abs(x)
    reversed_num = 0
    while remaining > 0:
        reversed_num *= 10
        reversed_num += (remaining % 10)
        remaining = int(remaining/10)
            
    if reversed_num >= INT_MAX or reversed_num <= INT_MIN:
        return 0
    return reversed_num if x > 0 else -reversed_num

out = reverse(123)
print(out)
