#include "../../utils/cpp/nodes.hpp"

class Solution {
private:
  int dfs(utils::TreeNode *node, int &maxDiameter) {
    if (!node)
      return 0;

    int leftHeight = dfs(node->left, maxDiameter);
    int rightHeight = dfs(node->right, maxDiameter);

    maxDiameter = std::max(maxDiameter, leftHeight + rightHeight);

    return 1 + std::max(leftHeight, rightHeight);
  }

public:
  int diameterOfBinaryTree(utils::TreeNode *root) {
    int maxDiameter = 0;
    dfs(root, maxDiameter);
    return maxDiameter;
  }
};
