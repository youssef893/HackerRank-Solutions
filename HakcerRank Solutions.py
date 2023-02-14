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


# Counting Valleys Solution
def countingValleys(steps, path):
    # Write your code here
    L=0
    V=0
    for s in path:
        if s == 'U':
            L += 1
           
            if L == 0:
                V += 1
        else:
            L -= 1
    return V



# Electronic Shop Solution
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    ans = -1
    for x in keyboards:
        for y in drives:
            if x + y <= b:
                ans = max(ans, x + y)
    return ans
