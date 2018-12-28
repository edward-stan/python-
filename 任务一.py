for i in range(1, 1000):
    j= 0
    for k in range(1, i):
        if i % k == 0:
            j = j + k
    if i == j:
        print(i)
