from random import choice


def quick_sort(a):

    if len(a) <= 1:
        return a
    else:
        q = choice(a)
        s_a, m_a, e_a = [], [], []
        for item in a:
            if item < q:
                s_a.append(item)
            elif item > q:
                m_a.append(item)
            else:
                e_a.append(item)
    return quick_sort(s_a) + e_a + quick_sort(m_a)
