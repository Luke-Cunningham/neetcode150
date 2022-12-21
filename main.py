def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    unique = set(nums)
    return len(unique) != len(nums)


if __name__ == '__main__':
    case1 = [1,2,3,1]
    containsDuplicate(case1)
