#include <stack>
#include <vector>

class Solution {
public:
  int numIslands(std::vector<std::vector<char>> &grid) {
    const size_t rows = grid.size();
    const size_t cols = grid[0].size();

    int numIslands = 0;

    for (size_t row{}; row < rows; ++row) {
      for (size_t col{}; col < cols; ++col) {
        if (grid[row][col] == '1') {
          std::stack<std::pair<size_t, size_t>> s;
          s.push({row, col});

          while (!s.empty()) {
            auto [r, c] = s.top();
            s.pop();
            grid[r][c] = '0';

            if (r - 1 != -1 && grid[r - 1][c] == '1')
              s.push({r - 1, c});
            if (c + 1 < cols && grid[r][c + 1] == '1')
              s.push({r, c + 1});
            if (r + 1 < rows && grid[r + 1][c] == '1')
              s.push({r + 1, c});
            if (c - 1 != -1 && grid[r][c - 1] == '1')
              s.push({r, c - 1});
          }

          ++numIslands;
        }
      }
    }

    return numIslands;
  }
};
