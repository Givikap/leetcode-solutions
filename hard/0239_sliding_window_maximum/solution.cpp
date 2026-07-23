#include <queue>
#include <vector>

class Solution {
public:
  std::vector<int> maxSlidingWindow(std::vector<int> &nums, int k) {
    std::priority_queue<std::pair<int, size_t>> pq;

    size_t i{};
    for (; i < k; ++i) {
      pq.push({nums[i], i});
    }

    std::vector<int> maxNums{pq.top().first};

    for (; i < nums.size(); ++i) {
      pq.push({nums[i], i});

      while (pq.top().second <= i - k)
        pq.pop();

      maxNums.push_back(pq.top().first);
    }

    return maxNums;
  }
};
