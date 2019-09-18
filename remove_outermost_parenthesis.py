def remove_outer_most_parenthesis(S):
    if S == "":
        return ""
    stack_im = []
    counter = 0
    temp_string = ""
    return_string = ""
    for i in S:
        if i == "(":
            counter = counter + 1
            temp_string = temp_string + i
        if i == ")":
            counter = counter - 1
            temp_string = temp_string + i
        if counter == 0:
            stack_im.append(temp_string)
            temp_string = ""
    for m in stack_im:
        return_string += str(m[1:-1])
    return return_string


s = "(()())(())(()(()))"
print(remove_outer_most_parenthesis(s))