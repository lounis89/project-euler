def solve() -> int:
    total_sum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            total_sum = total_sum + x
    return total_sum


def main():
    print(solve())


if __name__ == "__main__":
    main()
