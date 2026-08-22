#include "../../utils/cpp/nodes.hpp"

class Solution {
public:
  int rob(utils::TreeNode *root) {
    auto solve = [](this auto &&self,
                    utils::TreeNode *node) -> std::pair<int, int> {
      if (!node)
        return {0, 0};
      if (!node->left && !node->right)
        return {node->val, 0};

      auto [leftRobbed, leftNotRobbed] = self(node->left);
      auto [rightRobbed, rightNotRobbed] = self(node->right);

      return {node->val + leftNotRobbed + rightNotRobbed,
              std::max(leftRobbed, leftNotRobbed) +
                  std::max(rightRobbed, rightNotRobbed)};
    };

    auto [robbed, notRobbed] = solve(root);
    return std::max(robbed, notRobbed);
  }
};
