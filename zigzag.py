"""
n = 3
P   A   H   N
A P L S I I G
Y   I   R

n = 4
P     I    N
A   L S  I G
Y A   H R
P     I

solution: could not solve, copied from leetcode submissions
"""


class Solution(object):
    def convert(self, s, numRows):
        lines = [""] * numRows
        increment = numRows + (numRows - 2)

        if numRows == 1:
            return s

        try:
            for index in range(len(s))[::increment]:
                for index_down in range(numRows):
                    lines[index_down] += s[index + index_down]
                for index_up in range(numRows)[1:-1]:
                    lines[numRows - index_up - 1] += s[(index + numRows + index_up - 1)]
        except:
            pass

        return ''.join(lines)


if __name__ == '__main__':
    a = "PAYPALISHIRING"
    n = 4
    sol = Solution()
    print(sol.convert(a, n))
    

