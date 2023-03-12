from load_numbers import Numbers

def partition(tab, left, right):
    i = left-1
    pivot = tab[right]
    for j in range(left, right):
        if tab[j] <= pivot:
            i += 1
            temp = tab[j]
            tab[j] = tab[i]
            tab[i] = temp
    i += 1
    temp = tab[right]
    tab[right] = tab[i]
    tab[i] = temp

    return i

def quick_sort(tab, left, right):
    if  left < right:
        pivot = partition(tab, left, right)

        quick_sort(tab, left, pivot-1)
        quick_sort(tab, pivot+1, right)

def main():
    tab = Numbers.generate()
    quick_sort(tab, 0, len(tab)-1)

    print(tab)


if __name__ == "__main__":
    main()