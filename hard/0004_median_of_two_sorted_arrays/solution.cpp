#include <vector>

class Solution {
public:
  double findMedianSortedArrays(std::vector<int> &nums1,
                                std::vector<int> &nums2) {
    if (nums1.size() > nums2.size())
      swap(nums1, nums2);

    const size_t m = nums1.size();
    const size_t n = nums2.size();

    size_t left = 0;
    size_t right = m;

    while (left <= right) {
      size_t cut1 = (left + right) / 2;
      size_t cut2 = (m + n) / 2 - cut1;

      int l1 = (cut1 == 0) ? INT_MIN : nums1[cut1 - 1];
      int r1 = (cut1 == m) ? INT_MAX : nums1[cut1];
      int l2 = (cut2 == 0) ? INT_MIN : nums2[cut2 - 1];
      int r2 = (cut2 == n) ? INT_MAX : nums2[cut2];

      if (l1 > r2)
        right = cut1 - 1;
      else if (l2 > r1)
        left = cut1 + 1;
      else {
        if ((m + n) % 2 == 0)
          return (std::max(l1, l2) + std::min(r1, r2)) / 2.0;
        else
          return std::min(r1, r2);
      }
    }

    return 0.0;
  }
};
