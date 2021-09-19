def merge_sort(a):
    if len(a) <= 1:
        return a
    return merge(merge_sort(a[:(len(a)//2)]), merge_sort(a[(len(a)//2):]))


def merge(left, right):
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
