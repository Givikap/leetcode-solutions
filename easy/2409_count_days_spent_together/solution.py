class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        arriveAliceMonth, arriveAliceDay = tuple(
            map(int, arriveAlice.split("-"))
        )
        arriveBobMonth, arriveBobDay = tuple(map(int, arriveBob.split("-")))

        if arriveAliceMonth == arriveBobMonth:
            togetherStartMonth = arriveAliceMonth
            togetherStartDay = max(arriveAliceDay, arriveBobDay)
        else:
            togetherStartMonth = max(arriveAliceMonth, arriveBobMonth)
            togetherStartDay = (
                arriveAliceDay
                if arriveAliceMonth > arriveBobMonth
                else arriveBobDay
            )

        leaveAliceMonth, leaveAliceDay = tuple(map(int, leaveAlice.split("-")))
        leaveBobMonth, leaveBobDay = tuple(map(int, leaveBob.split("-")))

        if leaveAliceMonth == leaveBobMonth:
            togetherEndMonth = leaveAliceMonth
            togetherEndDay = min(leaveAliceDay, leaveBobDay)
        else:
            togetherEndMonth = min(leaveAliceMonth, leaveBobMonth)
            togetherEndDay = (
                leaveAliceDay
                if leaveAliceMonth < leaveBobMonth
                else leaveBobDay
            )

        daysCount = 0
        if togetherStartMonth > togetherEndMonth or (
            togetherStartMonth == togetherEndMonth
            and togetherStartDay > togetherEndDay
        ):
            return daysCount

        while togetherStartMonth < togetherEndMonth:
            daysCount += daysInMonth[togetherStartMonth - 1]
            togetherStartMonth += 1

        return daysCount + togetherEndDay - togetherStartDay + 1
