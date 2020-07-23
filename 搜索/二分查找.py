def binary_search1(nums, target):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (hi + lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if nums[lo] == target: return lo
    return -1


def binary_search2(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            lo = mid + 1
        elif target < nums[mid]:
            hi = mid - 1
    return -1


# 寻找某个数在数组中最左边插入的位置
def binary_search_left(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo


# 寻找某个数在数组中最右边插入的位置
def binary_search_right(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo


import bisect

ali = [1, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8]
ta = 4

print(binary_search1(ali, ta))
print(bisect.bisect_right(ali, ta))
