import sys


def solve(data: list, targets: list) -> list:
    dp = set()
    dp.add(0)
    result = []
    for weight in data:
        for no in list(dp):
            dp.add(no + weight)
            dp.add(abs(no - weight))

    for marble in targets:
        if marble in dp:
            result.append('Y')
        else:
            result.append('N')
    return result




n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
print(*solve(data, target))
