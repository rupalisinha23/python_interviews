"""
Medium of two sorted arrays/lists
Status: Could not solve
"""


class Solution:
    @staticmethod
    def median(list_a, list_b):
        m, n = len(list_a), len(list_b)
        if m > n:
            list_a, list_b, m, n = list_b, list_a, n, m
        if n == 0:
            raise ValueError

        i_min, i_max, half_len = 0, m, (m + n + 1) / 2
        while i_min <= i_max:
            i = int((i_min + i_max) / 2)
            j = int(half_len - i)
            if i < m and list_b[j-1] > list_a[i]:
                # i is too small, must increase it
                i_min = i + 1
            elif i > 0 and list_a[i-1] > list_b[j]:
                # i is too big, must decrease it
                i_max = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = list_b[j-1]
                elif j == 0:
                    max_of_left = list_a[i-1]
                else:
                    max_of_left = max(list_a[i-1], list_b[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: 
                    min_of_right = list_b[j]
                elif j == n: 
                    min_of_right = list_a[i]
                else: 
                    min_of_right = min(list_a[i], list_b[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    a = [1, 5, 8, 9]
    b = [6, 7, 10, 9, 11]
    print(Solution.median(a, b))
