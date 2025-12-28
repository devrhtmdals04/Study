#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        lowwer_s = s.lower()
        while left < right:
            while left < right and not lowwer_s[left].isalnum():
                left += 1
            while left < right and not lowwer_s[right].isalnum():
                right -= 1
            if lowwer_s[left] != lowwer_s[right]:
                return False
            left += 1
            right -= 1
        return True

        
# @lc code=end

