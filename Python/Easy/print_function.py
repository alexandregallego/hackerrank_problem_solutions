def returning_a_string_from_an_integer(n):
    x = ""
    if n < 151 and n >= 1:
        for i in range(1, n + 1):
            x += str(i)
    else:
        print("Need to enter a number between 1 and 150, including both")

    return x


def main():
    n = int(input())
    print(returning_a_string_from_an_integer(n))


if __name__ == '__main__':
    main()
