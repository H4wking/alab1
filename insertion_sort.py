def insertion_sort(lst):
    counter = 0
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            counter +=1
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return counter
