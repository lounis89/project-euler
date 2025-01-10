import time


def sum_of_dividers(n: int) -> int:
    counter = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            counter += 2
            if i * i == n:
                counter -= 1
    return counter


def calculate_triangular_numbers(max_dividers: int) -> int:
    i = 1
    while True:
        triangular_number = (i * (i + 1)) // 2
        dividers = sum_of_dividers(triangular_number)
        if dividers > max_dividers:
            return triangular_number
        i += 1


def main():
    start_time = time.time()
    print("result", calculate_triangular_numbers(500))
    print("Execution time:", time.time() - start_time)


if __name__ == "__main__":
    main()
