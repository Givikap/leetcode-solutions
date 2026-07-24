#include "../../utils/cpp/nodes.hpp"
#include <functional>

class Solution {
public:
  int findTilt(utils::TreeNode *root) {
    int tilt = 0;

    std::function<int(utils::TreeNode *)> subtreeSum =
        [&](utils::TreeNode *node) -> int {
      if (!node)
        return 0;

      int leftSum = subtreeSum(node->left);
      int rightSum = subtreeSum(node->right);

      tilt += abs(leftSum - rightSum);

      return node->val + leftSum + rightSum;
    };

    subtreeSum(root);
    return tilt;
  }
};
