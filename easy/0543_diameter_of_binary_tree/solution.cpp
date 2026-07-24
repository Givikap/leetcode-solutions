#include "../../utils/cpp/nodes.hpp"
#include <functional>

class Solution {
public:
  int diameterOfBinaryTree(utils::TreeNode *root) {
    int maxDiameter = 0;

    std::function<int(utils::TreeNode *)> dfs =
        [&](utils::TreeNode *node) -> int {
      if (!node)
        return 0;

      int leftHeight = dfs(node->left);
      int rightHeight = dfs(node->right);

      maxDiameter = std::max(maxDiameter, leftHeight + rightHeight);

      return 1 + std::max(leftHeight, rightHeight);
    };

    dfs(root);
    return maxDiameter;
  }
};
