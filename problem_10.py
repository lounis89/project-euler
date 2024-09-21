import time


def sieve_of_eratosthenes(n: int) -> int:
    prime_numbers = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            prime_numbers.append(i)
            for k in range(i * 2, n + 1, i):
                is_prime[k] = False
    return sum(prime_numbers)


def main():
    start_time = time.time()
    print(sieve_of_eratosthenes(2 * pow(10, 6)))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)


if __name__ == "__main__":
    main()
