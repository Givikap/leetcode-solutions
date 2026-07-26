#include <queue>
#include <vector>

class Solution {
public:
  int findCheapestPrice(int n, std::vector<std::vector<int>> &flights, int src,
                        int dst, int k) {
    std::vector<std::vector<std::pair<int, int>>> flightsMap(n);
    for (const std::vector<int> &flight : flights)
      flightsMap[flight[0]].push_back({flight[1], flight[2]});

    std::queue<std::tuple<int, int, int>> q;
    q.push({0, src, 0});

    std::vector<int> pricesMap(n, INT_MAX);
    pricesMap[src] = 0;

    while (!q.empty()) {
      auto [stops, from, price] = q.front();
      q.pop();

      if (stops > k)
        continue;

      for (const auto &[to, prc] : flightsMap[from]) {
        if (pricesMap[to] > price + prc) {
          pricesMap[to] = price + prc;
          q.push({stops + 1, to, pricesMap[to]});
        }
      }
    }

    return pricesMap[dst] != INT_MAX ? pricesMap[dst] : -1;
  }
};
