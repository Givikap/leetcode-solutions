#include <vector>

class Solution {
public:
  int oddCells(int m, int n, std::vector<std::vector<int>> &indices) {
    std::vector<int> rowsCounter(static_cast<size_t>(m), 0);
    std::vector<int> colsCounter(static_cast<size_t>(n), 0);

    for (const auto &index : indices) {
      ++rowsCounter[static_cast<size_t>(index[0])];
      ++colsCounter[static_cast<size_t>(index[1])];
    }

    int oddCount = 0;

    for (size_t r{}; r < rowsCounter.size(); ++r) {
      for (size_t c{}; c < colsCounter.size(); ++c) {
        if ((rowsCounter[r] + colsCounter[c]) % 2 == 1)
          ++oddCount;
      }
    }

    return oddCount;
  }
};
