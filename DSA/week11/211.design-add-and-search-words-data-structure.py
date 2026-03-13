#
# @lc app=leetcode id=211 lang=python
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary(object):

    def __init__(self):
        self.store = []

    def addWord(self, word):
        self.store.append(word)
        

    def search(self, word):
        for w in self.store:
            if len(w) != len(word):
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.':
                    i += 1
                else:
                    break
            if i == len(w):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

