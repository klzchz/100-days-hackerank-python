def diagonalDifference(arr):
    # Write your code here, O(n)
    #l, r = left sum, right sum
    l, r = 0, 0
    # single pass, grab both values
    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][-i-1]
    return abs(l-r)


arr = [
    [11 ,2 ,4],
    [4, 5 ,6],
    [10 ,8 ,-12]
]

print (diagonalDifference(arr))