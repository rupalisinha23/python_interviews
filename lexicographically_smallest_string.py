# problem: find the lexicographically smallest string by removing a character from a string
# e.g. a string "abc", now if we remove a character then we get: "ab", "bc", "ac", and the answer is "ab"

def solution(S):
    l = len(S)
    ans = ""
    # iterate through string
    for i in range (l-1):
        # first point where s[i]>s[i+1]
        if (S[i] > S[i + 1]):
            # form the string without the last char
            for j in range (l):
                if (i != j):
                    ans += S[j]
            return ans
    # remove the last char
    ans = S[0:l - 1]
    return ans
