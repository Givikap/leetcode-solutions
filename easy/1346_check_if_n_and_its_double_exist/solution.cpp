#include <unordered_set>
#include <vector>
class Solution {
public:
  bool checkIfExist(std::vector<int> &arr) {
    std::unordered_set<int> numsSet;

    for (const int &num : arr) {
      if (numsSet.find(num * 2) != numsSet.end() ||
          (num % 2 == 0 && numsSet.find(num / 2) != numsSet.end()))
        return true;

      numsSet.insert(num);
    }

    return false;
  }
};
