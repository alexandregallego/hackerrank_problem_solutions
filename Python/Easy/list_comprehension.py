def list_creation(x, y, z, n):

    permutations = [[i, j, k] for i in range(
        0, x+1) for j in range(0, y+1) for k in range(0, z+1)]
    filtered_elements = [sum(i) for i in permutations]
    indexes_to_drop = [i for i in range(
        0, len(filtered_elements)) if filtered_elements[i] == n]
    permutations_final = [lst for i, lst in enumerate(
        permutations) if i not in indexes_to_drop]

    return permutations_final


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list_creation(x, y, z, n))


if __name__ == '__main__':
    main()
