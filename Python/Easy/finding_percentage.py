def return_average(n, student_marks, query_name):
    relevant_list = student_marks[query_name]
    average = sum(relevant_list)/len(relevant_list)
    return '{:.2f}'.format(average)


def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(return_average(n, student_marks, query_name))


if __name__ == '__main__':
    main()
