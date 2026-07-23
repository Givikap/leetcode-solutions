#include <vector>

class Solution {
public:
  int maxProfit(std::vector<int> &prices) {
    int profit = 0;

    for (size_t i{}; i < prices.size(); ++i) {
      while (i < prices.size() - 1 && prices[i] > prices[i + 1])
        ++i;

      int buyPrice = prices[i];

      while (i < prices.size() - 1 && prices[i] < prices[i + 1])
        ++i;

      profit += prices[i] - buyPrice;
    }

    return profit;
  }
};
