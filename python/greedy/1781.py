import sys
from collections import deque
from heapq import heappop, heappush, heapify

input = sys.stdin.readline


def solve(data: list) -> int:
    n = len(data)

    heapify(data)
    time = 1
    answer = 0
    cups = []
    while data:
        tmp = heappop(data)
        answer -= tmp[1]
        heappush(cups, -tmp[1])
        if data and time == data[0][0]:
            while data and tmp[0] == data[0][0]:
                sub = heappop(data)
                if -sub[1] > cups[0]:
                    answer -= heappop(cups)
                    answer -= sub[1]
                    heappush(cups, -sub[1])
        time += 1
    return answer


data = []
for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    tmp[1] = -tmp[1]
    data.append(tmp)
print(solve(data))
