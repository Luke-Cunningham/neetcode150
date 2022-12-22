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


if __name__ == '__main__':
    case1 = [1,2,3,1]
    containsDuplicate(case1)

    s, t = "nagaram", "anagram"
    isAnagram(s, t)

    case1 = [-1, 0, 3, 5, 9, 12]
    search(case1, 5)

