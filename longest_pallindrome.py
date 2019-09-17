def longest_pallindrome(s):
    if s[::-1] == s:
        return s

    n = len(s)

    if n == 0:
        return ""

    if n == 1:
        return s

    if n == 2:
        return s[0]

    largest = 0
    return_string = ""

    for i in range(2, n+1):
        for j in range(0, n-i+1):
            temp = s[j:j+i]
            if temp == temp[::-1]:
                if i > largest:
                    largest = i
                    return_string = temp
    if return_string == "":
        return_string = s[0]
    return return_string


s = "abcda"
print(longest_pallindrome(s))