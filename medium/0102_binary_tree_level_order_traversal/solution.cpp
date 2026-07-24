#include "../../utils/cpp/nodes.hpp"
#include <queue>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> levelOrder(utils::TreeNode *root) {
    if (!root)
      return {};

    std::deque<utils::TreeNode *> dq{root};
    std::vector<std::vector<int>> levels;

    while (!dq.empty()) {
      std::vector<int> level;

      for (size_t _ = dq.size(); _ > 0; --_) {
        utils::TreeNode *node = dq.front();
        dq.pop_front();
        level.push_back(node->val);

        if (node->left)
          dq.push_back(node->left);
        if (node->right)
          dq.push_back(node->right);
      }

      levels.push_back(level);
    }

    return levels;
  }
};
