"""
Length of longest non-repeating substring
Status: Solved by Me
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_list = []
        max = 0
        count = 0
        for i in s:
            count += 1
            if i not in temp_list:
                temp_list.append(i)
                if len(temp_list) > max:
                    max = len(temp_list)
            else:
                temp_list.append(i)
                tmp_list_str = ''.join(temp_list)
                pos = tmp_list_str.find(i)
                temp_list = temp_list[pos+1:]
                if count == len(s):
                    if len(temp_list) > max:
                        max = len(temp_list)
                        return max
                if len(temp_list) > max:
                    max = len(temp_list)
        return max


if __name__ == '__main__':
    solution = Solution()
    input = "pwwkew"
    print(solution.lengthOfLongestSubstring(input))
