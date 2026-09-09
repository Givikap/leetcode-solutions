#include <vector>

class Solution {
public:
  std::vector<int> sortArray(std::vector<int> &nums) {
    size_t n = nums.size();

    auto siftDown = [&](size_t i) -> void {
      while (true) {
        size_t left = 2 * i + 1;
        size_t right = 2 * i + 2;

        size_t largest = i;

        if (left < n && nums[left] > nums[largest])
          largest = left;
        if (right < n && nums[right] > nums[largest])
          largest = right;

        if (largest == i)
          break;

        std::swap(nums[i], nums[largest]);
        i = largest;
      }
    };

    auto heapify = [&]() -> void {
      for (size_t i = n / 2 - 1; i != -1; --i)
        siftDown(i);
    };

    heapify();

    for (--n; n != -1; --n) {
      std::swap(nums[0], nums[n]);
      siftDown(0);
    }

    return nums;
  }
};
