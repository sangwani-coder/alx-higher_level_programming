#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}

    if roman_string is None or type(roman_string) is not str:
        return 0
    int_num = 0
    str_len = len(roman_string)

    for x in range(str_len):
        if x is (str_len - 1):
            int_num += roman_dic[roman_string[x]]
        else:
            if roman_dic[roman_string[x]] >= roman_dic[roman_string[x + 1]]:
                int_num += roman_dic[roman_string[x]]
            else:
                int_num -= roman_dic[roman_string[x]]
    return (int_num)
