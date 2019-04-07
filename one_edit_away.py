"""
replace/add/delete
abcd
abce

adfgt
adft

adfre
adgfre
"""


def find_diff_len(input1, input2):
    len2 = len(input2)
    itr1 = 0
    itr2 = 0
    count_dif = 0
    while itr2 < len2:
        if input1[itr1] == input2[itr2]:
            itr1 += 1
            itr2 += 1
        else:
            count_dif += 1
            itr1 += 1
            if count_dif >= 2:
                return False
    return True


def one_edit_away(input1, input2):
    len1 = len(input1)
    len2 = len(input2)
    if abs(len1 - len2) >= 2:
        return False
    elif input1 == input2:
        return True
    elif len1 == len2:
        count_diff = 0
        for i in range(0, len1):
            if input1[i] != input2[i]:
                count_diff += 1
        if count_diff > 1:
            return False
        else:
            return True
    elif len1 > len2:
        return find_diff_len(input1, input2)
    elif len2 > len1:
        return find_diff_len(input2, input1)


if __name__== '__main__':
    input1 = "dfgte"
    input2 = "dft"
    print(one_edit_away("abcde", "abcd"))  # should return True
    print(one_edit_away("abde", "abcde"))  # should return True
    print(one_edit_away("a", "a"))  # should return True
    print(one_edit_away("abcdef", "abqdef"))  # should return True
    print(one_edit_away("abcdef", "abccef"))  # should return True
    print(one_edit_away("abcdef", "abcde"))  # should return True
    print(one_edit_away("aaa", "abc"))  # should return False
    print(one_edit_away("abcde", "abc"))  # should return False
    print(one_edit_away("abc", "abcde"))  # should return False
    print(one_edit_away("abc", "bcc")) # should return False