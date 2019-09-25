def shell_sort(lst):
    counter = 0
    n = len(lst)
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, n):
            key = lst[i]
            j = i
            while j >= gap and lst[j - gap] > key:
                counter += 1
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = key
        gap //= 2
    return counter
