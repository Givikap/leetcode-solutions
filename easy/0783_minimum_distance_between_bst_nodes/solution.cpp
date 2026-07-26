#include "../../utils/cpp/nodes.hpp"
#include <stack>
#include <vector>

class Solution {
public:
  int minDiffInBST(utils::TreeNode *root) {
    std::stack<utils::TreeNode *> s;
    std::vector<int> values;

    utils::TreeNode *curr = root;

    while (!s.empty() || curr) {
      while (curr) {
        s.push(curr);
        curr = curr->left;
      }

      curr = s.top();
      s.pop();

      values.push_back(curr->val);
      curr = curr->right;
    }

    int minDiff = INT_MAX;
    for (size_t i = 0; i < values.size() - 1; ++i)
      minDiff = std::min(minDiff, abs(values[i] - values[i + 1]));

    return minDiff;
  }
};
