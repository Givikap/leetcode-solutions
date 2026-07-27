#include "../../utils/cpp/nodes.hpp"
#include <stack>

class Solution {
public:
  bool isValidBST(utils::TreeNode *root) {
    if (!root)
      return true;

    std::stack<std::tuple<utils::TreeNode *, long, long>> s;
    s.push({root, INT64_MIN, INT64_MAX});

    while (!s.empty()) {
      auto [node, left, right] = s.top();
      s.pop();

      if (left >= node->val || node->val >= right)
        return false;

      if (node->left)
        s.push({node->left, left, node->val});
      if (node->right)
        s.push({node->right, node->val, right});
    }

    return true;
  }
};
