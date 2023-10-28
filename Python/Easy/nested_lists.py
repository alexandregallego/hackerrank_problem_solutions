def main():
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])
    if len(list1) >= 2 and len(list1) <= 5:
        list_of_scores = []
        for i in list1:
            list_of_scores.append(i[1])
        first_max_score = min(list_of_scores)
        indexes_to_drop = [i for i, lst in enumerate(
            list1) if lst[1] == first_max_score]
        new_list = [lst for i, lst in enumerate(
            list1) if i not in indexes_to_drop]
        list_of_scores_2 = []
        for i in new_list:
            list_of_scores_2.append(i[1])
        second_max_score = min(list_of_scores_2)
        indexes_to_return = [i for i, lst in enumerate(
            new_list) if lst[1] == second_max_score]
        final_list = sorted([lst[0] for i, lst in enumerate(
            new_list) if i in indexes_to_return])
        for i in final_list:
            print(i)


if __name__ == '__main__':
    main()
