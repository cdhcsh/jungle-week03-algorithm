import sys


def solve(target: int, data: list):
    dp = [0] * (target + 1)
    dp[0] = 1
    for n in data:
        for i in range(0,target+1-n):
            dp[i+n] += dp[i]

    return dp[target]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    print(solve(target,data))