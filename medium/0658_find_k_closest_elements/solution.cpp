#include <algorithm>
#include <vector>

class Solution {
public:
  std::vector<int> findClosestElements(std::vector<int> &arr, int k, int x) {
    auto left = std::lower_bound(arr.begin(), arr.end(), x);
    auto right = left;

    while (right - left < k) {
      if (left != arr.begin() && right != arr.end()) {
        if (x - *(left - 1) <= *right - x)
          left--;
        else
          right++;
      } else if (left == arr.begin()) {
        right++;
      } else {
        --left;
      }
    }

    std::vector<int> neighbors;

    for (; left != right; ++left)
      neighbors.push_back(*left);

    return neighbors;
  }
};
