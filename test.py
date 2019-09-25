import random
import time
from selection_sort import selection_sort


for deg in range(7, 18):
    t = 0
    count = 0
    for i in range(5):
        a = list(range(2**deg))
        random.shuffle(a)
        s = time.time()
        count += selection_sort(a)
        t += time.time() - s
        print(t)
    print(deg)
    with open("selection_results.csv", "a") as f:
        f.write(str(deg) + "," + str(t/5) + "," + str(count/5) + "\n")

for deg in range(7, 18):
    t = 0
    count = 0
    a = list(range(2**deg))
    s = time.time()
    count += selection_sort(a)
    t += time.time() - s
    print(t)
    print(deg)
    with open("selection_results.csv", "a") as f:
        f.write(str(deg) + "," + str(t) + "," + str(count) + "\n")

for deg in range(7, 18):
    t = 0
    count = 0
    a = list(range(2**deg))
    a.reverse()
    s = time.time()
    count += selection_sort(a)
    t += time.time() - s
    print(t)
    print(deg)
    with open("selection_results.csv", "a") as f:
        f.write(str(deg) + "," + str(t) + "," + str(count) + "\n")

for deg in range(7, 18):
    t = 0
    count = 0
    for i in range(5):
        a = []
        for j in range(2**deg):
            a.append(random.choice([1, 2, 3]))
        random.shuffle(a)
        s = time.time()
        count += selection_sort(a)
        t += time.time() - s
        print(t)
    print(deg)
    with open("selection_results.csv", "a") as f:
        f.write(str(deg) + "," + str(t/5) + "," + str(count/5) + "\n")
