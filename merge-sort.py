from load_numbers import Numbers


def merge(arr, left, right):
    left_len = len(left)
    right_len = len(right)
    i = 0
    j = 0
    x = 0
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            arr[x] = left[i]
            i += 1
            x += 1
        else:
            arr[x] = right[j]
            j += 1
            x += 1

    while i < left_len:
        arr[x] = left[i]
        i += 1
        x += 1

    while j < right_len:
        arr[x] = right[j]
        j += 1
        x += 1


def merge_sort(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def main():
    arr = Numbers.generate()
    merge_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()

