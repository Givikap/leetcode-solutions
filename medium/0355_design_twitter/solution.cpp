#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Twitter {
public:
  Twitter() {
    tweetsMap = std::unordered_map<int, std::vector<std::pair<int, int>>>();
    followsMap = std::unordered_map<int, std::unordered_set<int>>();

    timestamp = 0;
  }

  void postTweet(int userId, int tweetId) {
    tweetsMap[userId].push_back({timestamp++, tweetId});
  }

  std::vector<int> getNewsFeed(int userId) {
    std::priority_queue<std::tuple<int, int, size_t>> pq;

    if (tweetsMap.find(userId) != tweetsMap.end()) {
      const auto &tweets = tweetsMap[userId];
      pq.push({tweets.back().first, userId, tweets.size() - 1});
    }

    for (const int &followeeId : followsMap[userId]) {
      if (followeeId == userId)
        continue;

      if (tweetsMap.find(followeeId) != tweetsMap.end()) {
        const auto &tweets = tweetsMap[followeeId];
        pq.push({tweets.back().first, followeeId, tweets.size() - 1});
      }
    }

    std::vector<int> feed;

    while (feed.size() < 10 && !pq.empty()) {
      auto [_, userId, i] = pq.top();
      pq.pop();

      const auto &tweets = tweetsMap[userId];
      feed.push_back(tweets[i].second);

      if (i > 0)
        pq.push({tweets[i - 1].first, userId, i - 1});
    }

    return feed;
  }

  void follow(int followerId, int followeeId) {
    followsMap[followerId].insert(followeeId);
  }

  void unfollow(int followerId, int followeeId) {
    followsMap[followerId].erase(followeeId);
  }

private:
  std::unordered_map<int, std::vector<std::pair<int, int>>> tweetsMap;
  std::unordered_map<int, std::unordered_set<int>> followsMap;

  int timestamp;
};
