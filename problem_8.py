import time
from functools import reduce


def solve(input_data: str) -> int:
    left = 0
    right = left + 13
    max_product = 0
    while right < len(input_data):
        product = reduce(lambda a, b: a * b, [int(x) for x in input_data[left:right]])
        if product > max_product:
            max_product = product
        left = left + 1
        right = right + 1
    return max_product


def load_input_data() -> str:
    input_data = open('problem_8_in.txt', 'r')
    content = input_data.read()
    return content


def main():
    data = load_input_data()
    start_time = time.time()
    print(solve(data))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)


if __name__ == "__main__":
    main()
