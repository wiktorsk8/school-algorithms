def power(x, n):
    if n == 0:
        return 1
    if n // 2 == 0:
        y = power(x, n//2)
        return y * y
    else:
        return x * power(x, n-1)

def main():
    print(power(3, 4))


if __name__ == "__main__":
    main()