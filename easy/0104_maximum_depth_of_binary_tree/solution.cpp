#include "../../utils/cpp/nodes.hpp"

class Solution {
public:
  int maxDepth(utils::TreeNode *root) {
    if (!root)
      return 0;

    return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
  }
};
