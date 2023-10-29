def count_substring(string, sub_string):
    new_list = []
    for i in range(0, len(string)):
        new_list.append(string[i:i+len(sub_string)])
    count_of_occurrences = new_list.count(sub_string)
    return count_of_occurrences
