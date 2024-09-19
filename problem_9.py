import time


def solve(n: int) -> int:
    i = 0
    j = 0
    k = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                    return i * j * k


def main():
    start_time = time.time()
    print(solve(1000))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)


if __name__ == "__main__":
    main()
