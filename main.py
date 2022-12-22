import collections


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    unique = set(nums)
    return len(unique) != len(nums)


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    tracker = collections.defaultdict(int)
    for x in s: tracker[x] += 1
    for x in t: tracker[x] -= 1
    return all(x == 0 for x in tracker.values())


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    r, c = len(matrix), len(matrix[0])
    start, end = 0, r * c - 1

    while start <= end:
        mid = (start + end) // 2
        num = matrix[mid / c][mid % c]

        if num == target:
            return True
        elif num < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


if __name__ == '__main__':
    case1 = [1,2,3,1]
    containsDuplicate(case1)

    s, t = "nagaram", "anagram"
    isAnagram(s, t)

    case1 = [-1, 0, 3, 5, 9, 12]
    search(case1, 5)

    m1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    searchMatrix(m1, 16)

