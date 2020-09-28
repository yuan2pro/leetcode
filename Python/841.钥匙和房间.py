#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start


class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        if not rooms:
            return False
        ans = {0}

        def dfs(room):
            for x in room:
                if x in ans:
                    continue
                ans.add(x)
                dfs(rooms[x])
            if len(ans) == len(rooms):
                return True
            return False
        return dfs(rooms[0])


# @lc code=end
