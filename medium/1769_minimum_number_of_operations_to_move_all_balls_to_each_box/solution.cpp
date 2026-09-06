#include <string>
#include <vector>

class Solution {
public:
  std::vector<int> minOperations(std::string boxes) {
    const size_t n = boxes.size();

    int acc = 0;
    int ones = 0;

    std::vector<int> operations(n, 0);

    for (size_t i{}; i < n; ++i) {
      operations[i] = (acc += ones);
      if (boxes[i] == '1')
        ++ones;
    }

    acc = 0;
    ones = 0;

    for (size_t i = n - 1; i != -1; --i) {
      operations[i] += (acc += ones);
      if (boxes[i] == '1')
        ++ones;
    }

    return operations;
  }
};
