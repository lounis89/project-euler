import time

"""
n -> n/2 if n is even
n -> 3n+1 if n is odd
"""


def solve(max_limit: int) -> int:
    max_chain_size = 0
    max_number = 0
    for i in range(2, max_limit):
        node = i
        chain_size = 1
        while node > 1:
            if node % 2 == 0:
                node = node / 2
            else:
                node = (node * 3) + 1
            chain_size = chain_size + 1

        if chain_size > max_chain_size:
            max_chain_size = chain_size
            max_number = i
    return max_number


def main():
    start_time = time.time()
    print("result", solve(1000000))
    print("Execution time:", time.time() - start_time)


if __name__ == "__main__":
    main()
