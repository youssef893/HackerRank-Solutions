# Migratory Birds Solution 
def migratoryBirds(arr):
    # Write your code here
    count = [0] * len(arr)
    for i in arr:
        count[i] += 1
    return count.index(max(count))


# Drawing Book Solution
def pageCount(n, p):
    # Write your code here
    return min(p//2,(n//2)-(p//2))



