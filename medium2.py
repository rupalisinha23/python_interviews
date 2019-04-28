"""
Medium of two sorted arrays/lists
Status: My Solution
"""


def medium(num_list):
    n = len(num_list)
    if n == 0:
        return 0.0
    elif n > 0 and n % 2 == 0:
        return float((num_list[int(n/2)] + num_list[(int(n/2)) - 1]) / 2)
    elif n > 0 and n % 2 != 0:
        return float(num_list[int((n - 1) / 2)])


class Solution:
    def find_medium_two_arrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        list.sort(nums1)
        return medium(nums1)


if __name__ == '__main__':
    a = [1, 5, 8, 9]
    b = [6, 7, 10, 9, 11]
    sol = Solution()
    print(sol.find_medium_two_arrays(a, b))
