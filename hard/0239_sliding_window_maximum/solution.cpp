#include <queue>
#include <vector>

class Solution {
public:
  std::vector<int> maxSlidingWindow(std::vector<int> &nums, int k) {
    std::deque<size_t> dq{0};

    size_t i = 1;
    for (; i < k; ++i) {
      while (!dq.empty() && nums[dq.back()] < nums[i])
        dq.pop_back();

      dq.push_back(i);
    }

    std::vector<int> maxNums{nums[dq.front()]};

    for (; i < nums.size(); ++i) {
      while (!dq.empty() && nums[dq.back()] < nums[i])
        dq.pop_back();

      dq.push_back(i);

      while (dq.front() <= i - k)
        dq.pop_front();

      maxNums.push_back(nums[dq.front()]);
    }

    return maxNums;
  }
};
