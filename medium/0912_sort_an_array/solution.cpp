#include <queue>
#include <vector>

class Solution {
public:
  std::vector<int> sortArray(std::vector<int> &nums) {
    std::deque<std::vector<int>> dq;
    for (const auto &num : nums)
      dq.push_back({num});

    while (dq.size() > 1) {
      auto v1 = dq.front();
      dq.pop_front();
      auto v2 = dq.front();
      dq.pop_front();

      size_t n1 = v1.size();
      size_t n2 = v2.size();

      size_t i1{};
      size_t i2{};

      std::vector<int> v3(n1 + n2);

      for (size_t i{}; i < n1 + n2; ++i) {
        if (i1 == n1 || (i2 != n2 && v1[i1] > v2[i2]))
          v3[i] = v2[i2++];
        else
          v3[i] = v1[i1++];
      }

      dq.push_back(v3);
    }

    return dq.front();
  }
};
