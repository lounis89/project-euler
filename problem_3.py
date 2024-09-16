def largest_prime_factor_of(n: int) -> int:
    prime_numbers = []
    i = 2
    while n > 1:
        if n % i == 0:
            prime_numbers.append(i)
            n = n // i
        else:
            i += 1

    return max(prime_numbers)


def main():
    print(largest_prime_factor_of(600851475143))


if __name__ == "__main__":
    main()
