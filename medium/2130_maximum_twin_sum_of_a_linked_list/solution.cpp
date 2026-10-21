#include "../../utils/cpp/nodes.hpp"
#include <stack>

class Solution {
public:
  int pairSum(utils::ListNode *head) {
    std::stack<utils::ListNode *> st;

    utils::ListNode *curr = head;
    while (curr) {
      st.push(curr);
      curr = curr->next;
    }

    int maxTwinSum = 0;

    curr = head;
    while (curr) {
      utils::ListNode *twin = st.top();
      st.pop();

      maxTwinSum = std::max(maxTwinSum, curr->val + twin->val);

      curr = curr->next;
    }

    return maxTwinSum;
  }
};
