from functools import wraps


def counter(fn):
    @wraps(fn)
    def helper(*args, **kargs):
        helper.invocations += 1
        return fn(*args, **kargs)
    helper.invocations = 0
    return helper


@counter
def coin_change(c, pos, s):

    if s == 0:
        return 1
    if s < 0:
        return 0
    if pos == 0:
        return 0

    return coin_change(c, pos-1, s) + coin_change(c, pos, s-c[pos-1])


coins = (1, 5, 10, 50)
summa = 100
x = coin_change(coins, len(coins), summa)

print(f'There are {x} ways to produce {summa} cents change')
print(f'number of func calls: {coin_change.invocations}')
