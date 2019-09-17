
def two_sum(nums, target):
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target. You may assume that
    each input would have exactly one solution, and you may not use
    the same element twice.
    :param nums:
    :param target:
    :return:
    """
    ix = 0
    for i in nums:
        rem = target - i
        if rem in nums and nums.index(rem) != ix:
            return [ix, nums.index(rem)]
        ix = ix + 1
    return []


s = [0, 4, 3, 0]

print(two_sum(s, 0))