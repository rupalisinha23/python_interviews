"""
If product of any three elements in a list is equal to a given number
"""


def multiplication_of_three(input_list, product):
    if product is None or input_list is None or len(input_list) == 0 or product == 0:
        return None

    def multiple_of_two(input_array, product):
        uniq_elements = set()
        for a in input_array:
            if product % a == 0:
                if a not in uniq_elements:
                    uniq_elements.add(a)
                b = product//a
                if b in uniq_elements:
                    return a, b
        return None
    index = 0
    for num in input_list:
        if product % num == 0:
            left = product//num
            dopplets = multiple_of_two(input_list[index+1:], left)
            if dopplets is not None:
                return num, dopplets
        index += 1
    return None


if __name__ == '__main__':
    input_list = [5, 2, 6, 3, 8, 9]
    product = 135
    print(multiplication_of_three(input_list, product))


