import time

GRID_SIZE = 20


def solve(input_data: str) -> int:
    flatten_matrix = [int(num) for num in input_data.split()]

    return max(check_horizontal(flatten_matrix),  # Horizontale
               check_product_with_offset(flatten_matrix, [0, 0, 0, 0]),  # Haut-bas
               check_product_with_offset(flatten_matrix, [0, 1, 2, 3]),  # Diagonale droite
               check_product_with_offset(flatten_matrix, [3, 2, 1, 0])  # Diagonale gauche
               )


def check_horizontal(flatten_matrix):
    max_product = 0
    for i in range(len(flatten_matrix) - 3):
        if i % GRID_SIZE < GRID_SIZE - 4:
            continue
        product = flatten_matrix[i] * flatten_matrix[i + 1] * flatten_matrix[i + 2] * flatten_matrix[i + 3]
        max_product = max(max_product, product)
    return max_product


def check_product_with_offset(int_list, offset) -> int:
    i, j, k, l = offset
    j += GRID_SIZE - 1
    k += (GRID_SIZE - 1) * 2
    l += (GRID_SIZE - 1) * 3
    max_product = 0

    while l < len(int_list) - 1 - offset[3]:
        max_product = max(max_product, int_list[i] * int_list[j] * int_list[k] * int_list[l])
        i += 1
        j += 1
        k += 1
        l += 1

    return max_product


def load_input_data() -> str:
    with open('problem_11_in.txt', 'r') as input_data:
        return input_data.read()


def main():
    data = load_input_data()
    start_time = time.time()
    print(solve(data))
    print("Execution time:", time.time() - start_time)


if __name__ == "__main__":
    main()
