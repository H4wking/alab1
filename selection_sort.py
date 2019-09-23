def selection_sort(lst):
    counter = 0
    for i in range(len(lst)):
        mn = i
        for j in range(i+1, len(lst)):
            if lst[mn] > lst[j]:
                counter += 1
                mn = j
        lst[i], lst[mn] = lst[mn], lst[i]
    return counter
