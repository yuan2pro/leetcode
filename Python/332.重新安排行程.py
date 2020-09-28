#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start

import collections


class Solution:
    def findItinerary(self, tickets):
        ticket_dict = collections.defaultdict(list)
        for ticket in tickets:
            ticket_dict[ticket[0]].append(ticket[1])
        path = ['JFK']

        def backtrack(cur_from):
            if len(path) == len(tickets) + 1:
                return True
            ticket_dict[cur_from].sort()
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)
                path.append(cur_to)
                if backtrack(cur_to):
                    return True
                path.pop()
                ticket_dict[cur_from].append(cur_to)
            return False
        backtrack("JFK")
        return path


# @lc code=end
