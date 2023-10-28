def return_runner_up_score(arr):
    list_1 = list(arr)
    if len(list_1) >= 2 and len(list_1) <= 10:
        maximum = max(list_1)
        for i in list_1:
            if i > maximum:
                maximum = i
        indexes_to_drop = [i for i in range(
            0, len(list_1)) if list_1[i] == maximum]
        new_list = [lst for i, lst in enumerate(
            list_1) if i not in indexes_to_drop]
        second_maximum = max(new_list)
        for i in new_list:
            if i > second_maximum:
                second_maximum = i
    else:
        print("You need to enter between 2 and 10 scores")

    return second_maximum


def main():
    n = int(input())
    arr = map(int, input().split())
    print(return_runner_up_score(arr))


if __name__ == '__main__':

    main()
