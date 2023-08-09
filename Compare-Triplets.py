def compareTriplets(a, b):
    alice, bob = 0, 0
    for i in range(3):
        if a[i] > b[i]:
             alice += 1
        if a[i] < b[i]:
            bob += 1
    return [alice,bob] 

print (compareTriplets([17 ,28, 30],[99, 16 ,8]))