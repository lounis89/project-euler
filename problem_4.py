def solve() -> int:
    max_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if is_palindrome(i * j) and (i * j) > max_palindrome:
                max_palindrome = i * j
    return max_palindrome


def is_palindrome(n: int) -> bool:
    n = str(n)
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] != n[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def main():
    print(solve())


if __name__ == "__main__":
    main()
