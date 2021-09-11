def get_memtable(dct, max_area):

    value = [m[0] for m in dct.values()]
    area = [m[1] for m in dct.values()]
    a, n = max_area + 1, len(value) + 1
    memtable = [[0] * a for _ in range(n)]

    for i in range(1, n):
        for j in range(1, a):
            if area[i-1] <= j:
                memtable[i][j] = max(
                    value[i-1] + memtable[i-1][j-area[i-1]],
                    memtable[i-1][j]
                    )
            else:
                memtable[i][j] = memtable[i-1][j]

    return memtable, value, area


def get_items(dct, max_area):

    memtable, value, area = get_memtable(dct, max_area)
    a, n = max_area, len(value)
    res, item_list = memtable[-1][-1], []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        elif res == memtable[i-1][a]:
            continue
        else:
            for k, v in dct.items():
                  if v == (value[i-1], area[i-1]):
                        item_list.append(k)
            res -= value[i-1]
            a -= area[i-1]

    return item_list


max_area = 10
dct = {
    'knife': (1, 1),
    'pen': (4, 5),
    'lazer': (8, 5)
}

v, *_ = get_memtable(dct, max_area)
k = get_items(dct, max_area)
print(f'max sum value: {v[-1][-1]}')
print(f'selected stuff: {k}')
