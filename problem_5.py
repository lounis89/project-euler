import time

"""
The script take 32 seconds to find the right solution
This is a brute-force version and can be optimized to reduce the execution time
"""


def solve() -> int:
    min_number = 20
    i = 1
    while i < 20:
        if min_number % i == 0:
            i = i + 1
        else:
            i = 1
            min_number = min_number + 1

    return min_number


def main():
    start_time = time.time()
    print(solve())
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)


if __name__ == "__main__":
    main()
