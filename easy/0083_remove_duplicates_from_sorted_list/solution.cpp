#include "../../utils/cpp/nodes.hpp"

class Solution {
public:
  utils::ListNode *deleteDuplicates(utils::ListNode *head) {
    utils::ListNode *curr = head;

    while (curr) {
      if (curr->next && curr->val == curr->next->val)
        curr->next = curr->next->next;
      else
        curr = curr->next;
    }

    return head;
  }
};
