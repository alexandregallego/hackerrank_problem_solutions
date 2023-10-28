def swap_case(s):
    new_str = ""
    for i in s:
        if i.isupper():
            converted_letter = i.lower()
            new_str += converted_letter
        else:
            converted_letter = i.upper()
            new_str += converted_letter
    return new_str
