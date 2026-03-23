#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#

# @lc code=start
#without memorization O(2^n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        res = []

        def backtrack(i, cur):
            if i == len(s):
                res.append(" ".join(cur.copy()))
                return
            
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
        backtrack(0, [])
        return res
    
#memorization O(n^3)
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        memo = {} # 이미 계산한 결과를 저장할 딕셔너리

        def backtrack(start):
            # 이미 계산한 인덱스라면 저장된 결과 반환
            if start in memo:
                return memo[start]
            
            # 끝까지 도달했다면 빈 문자열을 담은 리스트 반환 (조합의 완성)
            if start == len(s):
                return [""]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    # 현재 단어 이후의 부분 문자열로 만들 수 있는 결과들을 가져옴
                    sub_results = backtrack(end)
                    for sub in sub_results:
                        # 결과 조립 (뒤가 빈 문자열이면 단어만, 아니면 공백 추가)
                        res.append(word + ("" if sub == "" else " " + sub))
            
            # 계산된 결과를 메모리에 저장
            memo[start] = res
            return res

        return backtrack(0)


        
# @lc code=end

