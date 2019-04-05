"""
If product of any three elements in a list is equal to a given number
"""


def common_between_two_array(input_list_1, input_list_2):

    len1 = len(input_list_1)
    len2 = len(input_list_2)
    if len1 == 0 or len2 == 0:
        return None
    list.sort(input_list_1)
    list.sort(input_list_2)
    return_list = []
    i = 0
    j = 0
    while i < len1 and j < len2:
        print(i, input_list_1[i], j, input_list_2[j])
        if input_list_1[i] == input_list_2[j]:
            return_list.append(input_list_1[i])
            i += 1
            j += 1
        elif input_list_1[i] < input_list_2[i]:
            i += 1
        else:
            j += 1
    return return_list


if __name__ == '__main__':
    input_list1 = [5, 2, 6, 3, 8, 9]
    input_list2 = [5, 2, 8, 9]
    print(common_between_two_array(input_list1, input_list2))


