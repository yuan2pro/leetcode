#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low+high) // 2
            count = 0
            sub_sum = 0
            # 淘汰算法
            # 我们由前向后对nums进行划分，使其子数组和 <= mid，然后统计满足条件的数组数量
            # 若我们选的sum值过小，则满足条件的数量 > m，目标值应落在 [mid+1, high]
            # 若我们选的sum值过大，则满足条件的数量 < m，目标值应落在 [low, mid-1]
            for i in range(len(nums)):
                sub_sum+=nums[i]
                if sub_sum >mid:
                    count+=1
                    sub_sum = nums[i]
            # 注意：末尾还有一个子数组我们没有统计，这里把它加上
            count+=1
            if count>m:
                low = mid+1
            else:
                high = mid
        return low
                # @lc code=end
