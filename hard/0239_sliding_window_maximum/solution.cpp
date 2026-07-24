#include <queue>
#include <vector>

class Solution {
public:
  std::vector<int> maxSlidingWindow(std::vector<int> &nums, int k) {
    std::deque<size_t> dq;
    std::vector<int> maxNums;

    for (size_t i{}; i < nums.size(); ++i) {
      while (!dq.empty() && nums[dq.back()] < nums[i])
        dq.pop_back();

      dq.push_back(i);

      while (!dq.empty() && i >= k && dq.front() <= i - k)
        dq.pop_front();

      if (i >= k - 1)
        maxNums.push_back(nums[dq.front()]);
    }

    return maxNums;
  }
};
