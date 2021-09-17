def shaker_sort(array):

    swapped = True
    start = 0
    end = len(array) - 1

    while (swapped is True):

        swapped = False

        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        end -= 1

        if (not(swapped)):
            break
        swapped = False

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start += 1
    return array
