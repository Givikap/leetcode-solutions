#include <queue>
#include <vector>

class Solution {
public:
  int findKthLargest(std::vector<int> &nums, int k) {
    std::priority_queue<int> pq;

    for (const int &num : nums)
      pq.push(num);
    while (--k)
      pq.pop();

    return pq.top();
  }
};
