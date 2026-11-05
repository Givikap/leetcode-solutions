#include <cstdlib>
#include <vector>

class Solution {
public:
  int findTheDistanceValue(std::vector<int> &arr1, std::vector<int> &arr2,
                           int d) {
    int distance = 0;

    for (const auto &num1 : arr1) {
      bool distant = true;

      for (const auto &num2 : arr2) {
        if (abs(num1 - num2) <= d) {
          distant = false;
          break;
        }
      }

      if (distant)
        ++distance;
    }

    return distance;
  }
};
