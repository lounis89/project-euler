import time
from math import sqrt, floor


def is_prime(n: int) -> bool:
    if n % n == 0 and n % 1 == 0:
        for i in range(floor(sqrt(n)), 1, -1):
            if n % i == 0:
                return False
        return True
    return False


def solve(n: int) -> int:
    count = 0
    i = 1
    while count < n:
        i += 1
        if is_prime(i):
            count += 1
    return i


def main():
    start_time = time.time()
    print(solve(10001))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)


if __name__ == "__main__":
    main()
