def selection_sort(a):
    k = len(a)
    for i in range(k-1):
        x, ind = a[i], i
        for j in range(i+1, k):
            if x > a[j]:
                x, ind = a[j], j
        a[i], a[ind] = x, a[i]
    return a
