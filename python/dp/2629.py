import sys


def solve(data: list, targets: list) -> list:
    n = sum(data)
    dp = [0] * (n + 1)
    dp[0] = 1
    for weight in data:
        print(1,'~',n)
        for i in range(1,n):
            if i - weight >= 0:
                dp[i] += dp[i-weight]
            if i + weight <= n:
                dp[i] += dp[i+weight]
        print(dp)

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
solve(data, target)
