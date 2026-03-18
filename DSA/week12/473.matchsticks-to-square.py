#
# @lc app=leetcode id=473 lang=python
#
# [473] Matchsticks to Square
#

# @lc code=start
class Solution(object):
    def makesquare(self, matchsticks):
        total = sum(matchsticks)
        length = total // 4

        if total % 4 != 0:
            return False
        
        matchsticks.sort(reversed = True)
        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides += matchsticks[i]
                    if backtrack[i+1]:
                        return True
                sides[j] -= matchsticks[i]

                if sides[j] == 0:
                    break
            return False
        
        return backtrack(0)
        
# @lc code=end

