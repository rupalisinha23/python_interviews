import heapq

'''
Sample Input
6 <-- no of inputs
12
4
5
3
8
7
Sample Output
12.0
8.0
5.0
4.5
5.0
6.0
'''


def addNum(num, lowers, highers):
    if not lowers or num < -lowers[0]:
        heapq.heappush(lowers, -num)
    else:
        heapq.heappush(highers, num)


def rebalance(lowers, highers):
    if len(lowers) - len(highers) >= 2:
        heapq.heappush(highers, -heapq.heappop(lowers))
    elif len(highers) - len(lowers) >= 2:
        heapq.heappush(lowers, -heapq.heappop(highers))


def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0]) / 2
    if len(lowers) > len(highers):
        return float(-lowers[0])
    else:
        return float(highers[0])


def runningMedian(a):
    lowers = []  # max heap, vals should go in and come out negated
    highers = []  # min heap, vals should go in positive
    result = []
    for v in a:
        addNum(v, lowers, highers)
        rebalance(lowers, highers)
        result.append(round(getMedian(lowers, highers), 1))
    return result


if __name__ == '__main__':
    input = [1, 5, 12, 4, 5, 7]

    # running_list = []
    # for i in input:
    #     running_list.append(i)
    #     print(runningMedian(running_list))

    running_list = [1]
    # if empty_list return False else return True
    heapq.heapify(running_list)
    for i in input:
        heapq.heappush(running_list, i)
        print(list(running_list))
