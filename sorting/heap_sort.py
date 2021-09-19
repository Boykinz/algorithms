def massiv2kucha(a):

    k = len(a)
    for i in range(k):
        ind = i
        while ind != 0:
            parent = (ind - 1) // 2
            if a[ind] <= a[parent]:
                break
            a[ind], a[parent] = a[parent], a[ind]
            ind = parent
    return a


def removetopitem(kucha):

    top = kucha[0]
    k = len(kucha)
    kucha[0] = kucha[k-1]

    ind = 0
    while True:

        child1 = 2 * ind + 1
        child2 = 2 * ind + 2

        if child1 >= k:
            child1 = ind
        if child2 >= k:
            child2 = ind

        if (kucha[ind] >= kucha[child1]) and (kucha[ind] >= kucha[child2]):
            break

        if kucha[child1] >= kucha[child2]:
            swap = child1
        else:
            swap = child2

        kucha[ind], kucha[swap] = kucha[swap], kucha[ind]
        ind = swap

    kucha.pop()
    return top, kucha


def heap_sort(a):

    a = massiv2kucha(a)
    b, k = [], len(a)

    for i in range(k):
        top, a = removetopitem(a)
        b.insert(0, top)
    return b
