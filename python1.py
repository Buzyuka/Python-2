from math import floor
from random import randint


def bubble_sort(arr, comparator = lambda x, y: x > y):
    res = list(arr)
    swaped = False

    for i in range(len(res) - 1):
        for j in range(len(res) - i - 1):
            if comparator(res[j], res[j+1]):
                res[j], res[j+1] = res[j+1], res[j]
                swaped = True

        if not swaped:
            return res

    return res


def _merge(a1, a2):
    merged = []
    n = len(a1) + len(a2)
    i, j = 0, 0

    a1.append(float("inf"))
    a2.append(float("inf"))

    for _ in range(n):
        if a1[i] <= a2[j]:
            merged.append(a1[i])
            i += 1
        else:
            merged.append(a2[j])
            j += 1

    return merged


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    q = floor(len(arr) / 2)
    a1 = merge_sort(arr[0:q])
    a2 = merge_sort(arr[q:])

    return _merge(a1, a2)


# Функция для выбора iй порядковой статистики
def randomized_select(arr, p, r, i):
    if p == r:
        return arr[p]

    q = rangomized_partition(arr, p, r)
    k = q - p + 1

    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q+1, r, i - k)


def rangomized_partition(arr, p, r):
    i = randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def select(arr, i):
    return randomized_select(arr, 0, len(arr) - 1, i + 1)
