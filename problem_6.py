import time


def solve(n: int) -> int:
    return sum(range(1, n + 1)) ** 2 - sum(map(lambda x: x ** 2, range(1, n + 1)))


def main():
    start_time = time.time()
    print(solve(100))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)


if __name__ == "__main__":
    main()
