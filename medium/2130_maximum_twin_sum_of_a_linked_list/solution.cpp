#include "../../utils/cpp/nodes.hpp"
#include <vector>

class Solution {
public:
  int pairSum(utils::ListNode *head) {
    std::vector<int> vals;

    utils::ListNode *curr = head;
    while (curr) {
      vals.push_back(curr->val);
      curr = curr->next;
    }

    const size_t n = vals.size();

    int maxTwinSum = 0;

    for (size_t i{}; i < n; ++i)
      maxTwinSum = std::max(maxTwinSum, vals[i] + vals[n - i - 1]);

    return maxTwinSum;
  }
};
