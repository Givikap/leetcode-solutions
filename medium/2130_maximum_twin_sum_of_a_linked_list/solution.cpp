#include "../../utils/cpp/nodes.hpp"
#include <vector>

class Solution {
public:
  int pairSum(utils::ListNode *head) {
    if (!head)
      return 0;
    if (!head->next)
      return head->val;

    utils::ListNode *slow = head;
    utils::ListNode *fast = head->next;

    while (fast && fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }

    utils::ListNode *prev = NULL;
    utils::ListNode *curr = slow->next;
    utils::ListNode *next = NULL;

    while (curr) {
      next = curr->next;
      curr->next = prev;
      prev = curr;
      curr = next;
    }

    utils::ListNode *head1 = head;
    utils::ListNode *head2 = prev;

    int maxTwinSum = 0;

    while (head2) {
      maxTwinSum = std::max(maxTwinSum, head1->val + head2->val);
      head1 = head1->next;
      head2 = head2->next;
    }

    return maxTwinSum;
  }
};
