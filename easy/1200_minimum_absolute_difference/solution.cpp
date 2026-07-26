#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> minimumAbsDifference(std::vector<int> &arr) {
    std::sort(arr.begin(), arr.end());

    int minDifference = INT_MAX;
    std::vector<std::vector<int>> differences;

    for (size_t i = 1; i < arr.size(); ++i) {
      int currDifference = arr[i] - arr[i - 1];

      if (currDifference < minDifference) {
        differences.clear();
        minDifference = currDifference;
      }

      if (currDifference == minDifference)
        differences.push_back({arr[i - 1], arr[i]});
    }

    return differences;
  }
};
