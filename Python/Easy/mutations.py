def mutate_string(string, position, character):
    ls = list(string)
    ls[position] = character
    new_str = ('').join(ls)
    return new_str
