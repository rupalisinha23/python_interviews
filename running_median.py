import heapq


class Solution:
    def addNum(self, num, lowers, highers):
        if not lowers or num < - lowers[0]:
            heapq.heappush(lowers, -num)
        else:
            heapq.heappush(highers, num)

    def reBalance(self, lowers, highers):
        if len(highers) - len(lowers) >= 2:
            heapq.heappush(lowers, -(heapq.heappop(highers)))
        elif len(lowers) - len(highers) >= 2:
            heapq.heappush(highers, -(heapq.heappop(lowers)))

    def getMedian(self, lowers, highers):
        if len(lowers) == len(highers):
            return (-lowers[0] + highers[0])/2
        elif len(lowers) > len(highers):
            return -(lowers[0])
        else:
            return highers[0]

    def runningMedian(self, input):
        lowers = []  # max heap, values should go in and come out negated
        highers = []  # min heap, values should go in positive
        result = []
        for v in input:
            self.addNum(v, lowers, highers)
            self.reBalance(lowers, highers)
            result.append(self.getMedian(lowers, highers))
        return result


if __name__ == '__main__':
    sol = Solution()
    input = [1, 5, 9, 7, 3, 4]
    print(sol.runningMedian(input))
