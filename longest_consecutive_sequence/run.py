### Solution 1 - this will only work if there's only 1 sequence

def find_longest_subset(arr):
    seen = set()
    
    for n in arr:
        if (n in seen):
            continue
        
        if (n - 1) in arr:
            seen.add(n)
            seen.add(n - 1)
        
        if (n + 1) in arr:
            seen.add(n)
            seen.add(n + 1)
            
        print(seen)
            
    return len(seen)
        
        
length = find_longest_subset([100, 4, 200, 1, 3, 2])
print length

### Solution 2 - with multiple sequences




### Solution 3 - with overlapping sequences? buhahaha
