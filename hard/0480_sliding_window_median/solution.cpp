#include <functional>
#include <queue>
#include <vector>

class Solution {
public:
  std::vector<double> medianSlidingWindow(std::vector<int> &nums, int k) {
    std::priority_queue<std::pair<int, size_t>> maxHeap;
    std::priority_queue<std::pair<int, size_t>,
                        std::vector<std::pair<int, size_t>>,
                        std::greater<std::pair<int, size_t>>>
        minHeap;

    std::vector<int> heapMap(nums.size(), -1);
    std::vector<int> staleMap(nums.size(), 0);

    size_t i{};
    for (; i < k; ++i) {
      minHeap.push({nums[i], i});
      heapMap[i] = 1;
    }

    for (size_t _{}; _ < k / 2; ++_) {
      auto [num, j] = minHeap.top();
      minHeap.pop();
      maxHeap.push({num, j});
      heapMap[j] = 0;
    }

    size_t maxHeapSize = maxHeap.size();
    size_t minHeapSize = minHeap.size();

    std::vector<double> medians;
    medians.reserve(nums.size() - k);

    if (k % 2 == 1)
      medians.push_back(minHeap.top().first);
    else
      medians.push_back(maxHeap.top().first / 2.0 + minHeap.top().first / 2.0);

    for (; i < nums.size(); ++i) {
      staleMap[i - k] = staleMap[i - k] + 1;

      if (heapMap[i - k] == 0)
        --maxHeapSize;
      else
        --minHeapSize;

      if (!maxHeap.empty() && nums[i] <= maxHeap.top().first) {
        maxHeap.push({nums[i], i});
        heapMap[i] = 0;
        ++maxHeapSize;
      } else {
        minHeap.push({nums[i], i});
        heapMap[i] = 1;
        ++minHeapSize;
      }

      if (minHeapSize > maxHeapSize + 1) {
        auto [num, j] = minHeap.top();
        minHeap.pop();

        while (staleMap[j]) {
          --staleMap[j];
          std::tie(num, j) = minHeap.top();
          minHeap.pop();
        }

        maxHeap.push({num, j});

        heapMap[j] = 0;
        ++maxHeapSize;
        --minHeapSize;
      } else if (maxHeapSize > minHeapSize) {
        auto [num, j] = maxHeap.top();
        maxHeap.pop();

        while (staleMap[j]) {
          --staleMap[j];
          std::tie(num, j) = maxHeap.top();
          maxHeap.pop();
        }

        minHeap.push({num, j});

        heapMap[j] = 1;
        --maxHeapSize;
        ++minHeapSize;
      }

      while (!maxHeap.empty() && staleMap[maxHeap.top().second]) {
        --staleMap[maxHeap.top().second];
        maxHeap.pop();
      }
      while (!minHeap.empty() && staleMap[minHeap.top().second]) {
        --staleMap[minHeap.top().second];
        minHeap.pop();
      }

      if ((maxHeapSize + minHeapSize) % 2 == 1)
        medians.push_back(minHeap.top().first);
      else
        medians.push_back(maxHeap.top().first / 2.0 +
                          minHeap.top().first / 2.0);
    }

    return medians;
  }
};
