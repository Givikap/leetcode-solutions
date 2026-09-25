class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five_counter = 0
        ten_counter = 0

        for bill in bills:
            if bill == 5:
                five_counter += 1
            elif bill == 10:
                if not five_counter:
                    return False

                five_counter -= 1
                ten_counter += 1
            else:
                if ten_counter > 0 and five_counter > 0:
                    five_counter -= 1
                    ten_counter -= 1
                elif five_counter >= 3:
                    five_counter -= 3
                else:
                    return False

        return True
