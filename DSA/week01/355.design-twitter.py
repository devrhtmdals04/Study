#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#
from collections import defaultdict
import heapq
# @lc code=start
class Twitter(object):

    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.posts[userId].append([self.time, tweetId])
        if len(self.posts) > 10:
            self.posts[userId].pop(0)
        

    def getNewsFeed(self, userId):
        followees = self.follows[userId]
        followees.add(userId)

        maxHeap = []

        for followerId in followees:
            user_tweaks = self.posts[followerId]

            if user_tweaks:
                index = len(user_tweaks) - 1
                time, tweet_Id = user_tweaks[index]
                heapq.heappush(maxHeap, (-time, tweet_Id, followerId, index))
        res = []
        while maxHeap and len(res) < 10:
            nTime, tweet_Id, followerId, index = heapq.heappop(maxHeap)
            res.append(tweet_Id)

            if index > 0:
                prev_index = index - 1
                prev_time, prev_tweet_id = self.posts[followees][prev_index]
                heapq.heappush(maxHeap, (-prev_time, prev_tweet_id, followees, prev_index))
        return res
        

    def follow(self, followerId, followeeId):
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

