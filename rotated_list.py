"""
if two lists are rotation of each other
    [1,2,3,4,5,6,7]
    [4,5,6,7,1,2,3]
"""


def rotated_or_not(input_list1, input_list2):
    len_a = len(input_list1)
    len_b = len(input_list2)

    if len_a != len_b:
        return False

    key = input_list1[0]
    key_index = -1
    index = 0

    for b in input_list2:
        if b == key:
            key_index = index
        index += 1

    if key_index == -1:
        return False
    else:
        for i in range(0, len_a):
            j = (i + key_index)%len_a
            if input_list1[i] != input_list2[j]:
                return False
    return True


if __name__ == '__main__':
    input_list1 = [1, 2, 3, 4, 5, 6, 7]
    input_list2 = [4, 5, 7, 6, 1, 2, 3]
    print(rotated_or_not(input_list1, input_list2))

