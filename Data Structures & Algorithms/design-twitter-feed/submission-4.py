# # a set to store the followees of a certain user
# # USERS FOLLOW THEMSELVES AND REQUIRE THEIR OWN TWEETS IN THEIR NEWS FEEDS**
# followMap- 
# (1: (1,4), 2: (2, 1), 3: (3, 4), 4: (4, 1))

# # a hash map that stores the user as the key, and their time stamps + tweetIds in a list as the value
# tweetMap-
# {1:[(-2, 3), (-7, 8)], 2: [(0, 1), (-1, 2)], 3: [(-3, 4), (-4, 5), (-5, 6)], 4: [(-6, 7)]}

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId:int) -> List:
        newsFeed = []
        minHeap = []

        self.followMap[userId].add(userId)
        # get the first most recent tweets for each followee and add to minHeap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (time, tweetId, followeeId, index - 1))
        
        while minHeap and len(newsFeed) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            newsFeed.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (time, tweetId, followeeId, index - 1))
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# getNewsFeed-
# Nigels newsfeed would contain
# Nigels tweets: (-2, 3) (-7, 8) Garrys tweets: (-6, 7)
# we pull most recent tweets from both followees tweetMaps first and add it into a minHeap
# then we pop the first value from the minHeap (the lowest value which follows the negative ranking of the timestamps ie max = -8, so 
# tweet with timestamp = -8 is the most recent tweet and is the first tweet in the feed) 
# after we pop the first value, we add it to our newsFeed/result. Then we push the next tweet for that user whose tweet we just popped from
# the minHeap if any, and start the loop over.