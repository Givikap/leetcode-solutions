#include <numeric>
#include <stack>
#include <unordered_map>
#include <vector>

class Solution {
public:
  int findTargetSumWays(std::vector<int> &nums, int target) {
    const size_t n = nums.size();
    const size_t offset =
        static_cast<size_t>(accumulate(nums.begin(), nums.end(), 0));

    std::vector<std::vector<int>> memo(n + 1,
                                       std::vector<int>(2 * offset + 1, -1));

    std::stack<std::pair<size_t, int>> st;
    st.push({0, 0});

    while (!st.empty()) {
      auto [i, curr] = st.top();

      if (i == n) {
        memo[i][curr + offset] = curr == target ? 1 : 0;
        st.pop();
      } else {
        if (memo[i + 1][curr - nums[i] + offset] == -1)
          st.push({i + 1, curr - nums[i]});
        if (memo[i + 1][curr + nums[i] + offset] == -1)
          st.push({i + 1, curr + nums[i]});

        if (st.top().first == i) {
          memo[i][curr + offset] = memo[i + 1][curr + nums[i] + offset] +
                                   memo[i + 1][curr - nums[i] + offset];
          st.pop();
        }
      }
    }

    return memo[0][offset];
  }
};
