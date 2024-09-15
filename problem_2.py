def solve() -> int:
    total_sum = 0
    fib = 2
    n_1 = 1
    n_2 = 0
    while fib < 4e6:
        fib = n_1 + n_2
        n_1 = n_2
        n_2 = fib
        if fib % 2 == 0:
            total_sum = total_sum + fib
    return total_sum


def main():
    print(solve())


if __name__ == "__main__":
    main()
