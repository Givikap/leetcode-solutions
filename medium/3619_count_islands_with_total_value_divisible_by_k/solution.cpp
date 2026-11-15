#include <stack>
#include <vector>

class Solution {
public:
  int countIslands(std::vector<std::vector<int>> &grid, int k) {
    const size_t rows = grid.size();
    const size_t cols = grid[0].size();

    int islandsCount = 0;

    for (size_t row{}; row < rows; ++row) {
      for (size_t col{}; col < cols; ++col) {
        if (grid[row][col] != 0) {
          std::stack<std::pair<size_t, size_t>> st;
          st.push({row, col});

          long long islandValue = 0;

          while (!st.empty()) {
            auto [r, c] = st.top();
            st.pop();

            islandValue += static_cast<long long>(grid[r][c]);
            grid[r][c] = 0;

            if (r - 1 != -1 && grid[r - 1][c] != 0)
              st.push({r - 1, c});
            if (c + 1 < cols && grid[r][c + 1] != 0)
              st.push({r, c + 1});
            if (r + 1 < rows && grid[r + 1][c] != 0)
              st.push({r + 1, c});
            if (c - 1 != -1 && grid[r][c - 1] != 0)
              st.push({r, c - 1});
          }

          if (islandValue % static_cast<long long>(k) == 0ll)
            ++islandsCount;
        }
      }
    }

    return islandsCount;
  }
};
