#include <numeric>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<int> minOperations(std::string boxes) {
    const size_t n = boxes.size();

    std::vector<int> onesIndices;

    for (size_t i{}; i < n; ++i) {
      if (boxes[i] == '1')
        onesIndices.push_back(static_cast<int>(i));
    }

    std::vector<int> operations(n, 0);

    for (size_t i{}; i < n; ++i) {
      operations[i] = std::accumulate(
          onesIndices.begin(), onesIndices.end(), 0,
          [&](int acc, int j) { return acc + abs(static_cast<int>(i) - j); });
    }

    return operations;
  }
};
