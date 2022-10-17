def reversed(a):
    n = len(a)-1
    b = ""
    while n >= 0:
        b += a[n]
        n -= 1
    return b

def bubbleSort(a, bool):
    if isinstance(a, str):
        b = ""
        a_list = sorted(a, reverse=bool)
        n = 0
        while n < len(a_list):
            b += a_list[n]
            n += 1
        return b
