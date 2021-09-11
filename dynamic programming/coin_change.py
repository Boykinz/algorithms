def coin_change(coins, value):

    n, v = len(coins) + 1, value + 1
    memtable, x = [1] * v, [0] * v

    for c in coins[1:]:
        for j in range(v):
            if c > j:
                x[j] = memtable[j]
            else:
                x[j] = memtable[j] + x[j-c]
        memtable = x

    return memtable


coins = (1, 5, 10, 50)
value = 200


v = coin_change(coins, value)
print(f'There are {v[-1]} ways to produce {value} cents change')
