#include <stack>
#include <vector>

class Solution {
public:
  int closedIsland(std::vector<std::vector<int>> &grid) {
    const size_t rows = grid.size();
    const size_t cols = grid[0].size();

    int closedIslandsCount = 0;

    for (size_t row{}; row < rows; ++row) {
      for (size_t col{}; col < cols; ++col) {
        if (!grid[row][col]) {
          std::stack<std::pair<size_t, size_t>> st;
          st.push({row, col});

          bool closed = true;

          while (!st.empty()) {
            auto [r, c] = st.top();
            st.pop();

            grid[r][c] = 1;

            if (r != 0 && grid[r - 1][c] == 0)
              st.push({r - 1, c});
            else if (r == 0)
              closed = false;
            if (c + 1 < cols && grid[r][c + 1] == 0)
              st.push({r, c + 1});
            else if (c + 1 == cols)
              closed = false;
            if (r + 1 < rows && grid[r + 1][c] == 0)
              st.push({r + 1, c});
            else if (r + 1 == rows)
              closed = false;
            if (c != 0 && grid[r][c - 1] == 0)
              st.push({r, c - 1});
            else if (c == 0)
              closed = false;
          }

          if (closed)
            ++closedIslandsCount;
        }
      }
    }

    return closedIslandsCount;
  }
};
