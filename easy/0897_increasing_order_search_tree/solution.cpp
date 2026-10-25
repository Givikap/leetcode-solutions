#include "../../utils/cpp/nodes.hpp"

class Solution {
private:
  utils::TreeNode *increasingBST_(utils::TreeNode *node,
                                  utils::TreeNode *tail = nullptr) {
    if (!node)
      return tail;

    utils::TreeNode *temp = increasingBST_(node->left, node);
    node->left = nullptr;
    node->right = increasingBST_(node->right, tail);
    return temp;
  }

public:
  utils::TreeNode *increasingBST(utils::TreeNode *root) {
    return increasingBST_(root);
  }
};
