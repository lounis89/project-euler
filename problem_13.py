import time


def solve(input_data: str) -> int:
    flatten_matrix = [int(num) for num in input_data.split()]
    return sum(flatten_matrix)


def load_input_data() -> str:
    with open('problem_13_in.txt', 'r') as input_data:
        return input_data.read()


def main():
    data = load_input_data()
    start_time = time.time()
    print(solve(data))
    print("Execution time:", time.time() - start_time)


if __name__ == "__main__":
    main()
